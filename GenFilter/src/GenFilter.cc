// -*- C++ -*-
//
// Package:    GenFilter
// Class:      GenFilter
// 
/**\class GenFilter GenFilter.cc Generator/GenFilter/src/GenFilter.cc

   Description: Filters unobserverable events of interest

   Implementation:

*/
//
// Original Author:  Nathaniel Odell
//         Created:  Wed Oct  2 18:48:53 CDT 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Generator data formats
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "TFile.h"
#include "TH1D.h"
#include "TMath.h"

using namespace reco;
using namespace edm;
using namespace std;

//
// class declaration
//

class GenFilter : public EDFilter {
public:
  explicit GenFilter(const ParameterSet&);
  ~GenFilter();

  static void fillDescriptions(ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual bool filter(Event&, const EventSetup&);
  virtual void endJob() ;

  virtual bool beginRun(Run&, EventSetup const&);
  virtual bool endRun(Run&, EventSetup const&);
  virtual bool beginLuminosityBlock(LuminosityBlock&, EventSetup const&);
  virtual bool endLuminosityBlock(LuminosityBlock&, EventSetup const&);

  // ----------member data ---------------------------
  vector<double> _ptmin;
  vector<double> _ptminloose; //if different cut for trailing
  vector<double> _etamax;
  vector<double> _etamin;
  vector<int>    _id;        //pdg id of particles of interest
  unsigned       _naccepted; //how many final state particles are needed
  unsigned       _nloose;    //how many loose final state particles there can be
  unsigned       _nhadtaus;  //how many hadronic taus are needed
  int            _verbose;
};

GenFilter::GenFilter(const ParameterSet& iConfig):
  _ptmin(iConfig.getUntrackedParameter<vector<double>>("ptmin"))
  , _ptminloose(iConfig.getUntrackedParameter<vector<double>>("ptminloose"))
  , _etamax(iConfig.getUntrackedParameter<vector<double>>("etamax"))
  , _etamin(iConfig.getUntrackedParameter<vector<double>>("etamin"))
  , _id(iConfig.getUntrackedParameter<vector<int>>("id"))
  , _naccepted(iConfig.getUntrackedParameter<unsigned>("naccepted", 0))
  , _nloose(iConfig.getUntrackedParameter<unsigned>("nloose", 0))
  , _nhadtaus(iConfig.getUntrackedParameter<unsigned>("nhadtaus", 0))
  , _verbose(iConfig.getUntrackedParameter<int>("verbose", 0))

{
  //now do what ever initialization is needed
  unsigned sizes = _id.size();
  if(_ptmin.size() != sizes || _etamin.size() != sizes || _etamax.size() != sizes
     || (_ptminloose.size() > 0 && _ptminloose.size() != sizes))
    throw "GenFilter cut vectors have different sizes!";

  if((find(_id.begin(), _id.end(), 15) == _id.end()) && _nhadtaus > 0)
    throw "GenFilter not selecting taus but requires hadronic taus!";
  
  if(_verbose > 0) {
    printf("GenFilter::GenFilter --> Cuts for decay products of:\n");
    for(unsigned i = 0; i < sizes ; ++i)
      printf("%i: ptmin = %.2f GeV/c, %.2f > eta > %.2f\n",
	   _id[i], _ptmin[i], _etamax[i], _etamin[i]);
    printf("Requiring at least %u accepted final state particles and %u hadronic taus\n",
	   _naccepted, _nhadtaus);

    if(_ptminloose.size() > 0) {
      printf("GenFilter::GenFilter --> Loose cuts for decay products of:\n");
      for(unsigned i = 0; i < sizes ; ++i)
	printf("%i: ptmin = %.2f GeV/c (%.2f > eta > %.2f)\n",
	       _id[i], _ptminloose[i], _etamax[i], _etamin[i]);
      printf("Allowing up to %u accepted loose final state particles\n",
	     _nloose);
    }
  }
}


GenFilter::~GenFilter()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}

// ------------ method called on each new Event  ------------
bool GenFilter::filter(Event& iEvent, const EventSetup& iSetup)
{
  Handle<GenParticleCollection> genParticleColl;
  iEvent.getByLabel("genParticles", genParticleColl);

  unsigned acceptCount = 0; //counting accepted final state particles
  unsigned looseCount = 0; //counting accepted loose final state particles
  unsigned hadTauCount = 0; //counting accepted hadronic taus
  unsigned particleCount = 0;

  if(_verbose > 3) 
    cout << "Printing particle collection for " << iEvent.id() << endl;
   else if(_verbose > 2)
     cout << "Printing interesting particles for " << iEvent.id() << endl;
   else if(_verbose > 1)
     cout << "Printing accepted particles for " << iEvent.id() << endl;
   if(_verbose > 1)
     cout << "index: pdg, status,   pt,    eta,    m,    N(daughters)" << endl;
  
  for (GenParticleCollection::const_iterator iGenPart = genParticleColl->begin(); iGenPart != genParticleColl->end(); ++iGenPart) {
    const GenParticle myParticle = GenParticle(*iGenPart);
    ++particleCount;
    if(_verbose > 3)
      printf("%4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu\n",
	     particleCount, myParticle.pdgId(),
	     myParticle.status(), myParticle.pt(),
	     myParticle.eta(), myParticle.mass(),
	     myParticle.numberOfDaughters());
    if((myParticle.status() == 1 && myParticle.numberOfDaughters() != 0) ||
       (myParticle.status() != 1 && myParticle.numberOfDaughters() == 0))
      printf("Error! Conflicting status! %4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu\n",
	     particleCount, myParticle.pdgId(),
	     myParticle.status(), myParticle.p4().pt(),
	     myParticle.eta(), myParticle.mass(),
	     myParticle.numberOfDaughters());

    //do tau check specially
    if(abs(myParticle.pdgId()) == 15 && //is a tau
       find(_id.begin(),_id.end(),15) != _id.end()) { //cutting on hadronic taus

      int nu_index = -1; //check if this tau decays or undergoes FSR, store neutrino index
      bool hadronic = true; //check that it's a hadronic decay
      for(unsigned index = 0; index < myParticle.numberOfDaughters(); ++index) {
	if(abs(myParticle.daughter(index)->pdgId()) == 16) nu_index = index;
	hadronic &= (abs(myParticle.daughter(index)->pdgId()) != 13 &&
		     abs(myParticle.daughter(index)->pdgId()) != 11); 
      }
      if(!hadronic || nu_index < 0) continue;

      //get index of the cuts
      unsigned id = 0;
      for(unsigned i = 0; i < _id.size(); ++i)
	if(_id[i] == 15) id = i;
      
      auto lv = myParticle.p4() - myParticle.daughter(nu_index)->p4(); //assume the hadronic tau LV = tau - tau neutrino
      if(lv.pt() > _ptmin[id] &&
	 lv.eta() > _etamin[id] &&
	 lv.eta() < _etamax[id]) {
	++hadTauCount;
	if(_verbose > 1) {
	  printf("%4u: %5i,   %2i, %8.2f, %12.2f, %8.2f, %3lu (Accepted)\n Tau daughters pdgs:",
		 particleCount,
		 myParticle.pdgId(), myParticle.status(), myParticle.pt(),
		 myParticle.eta(), myParticle.mass(),
		 myParticle.numberOfDaughters());
	  for(unsigned index = 0; index < myParticle.numberOfDaughters(); ++index)
	    cout << " " << myParticle.daughter(index)->pdgId();
	  cout << endl;
	}
      } else if(_verbose > 2) {
	printf("%4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu (Rejected)\n Tau daughters pdgs:",
	       particleCount,
	       myParticle.pdgId(), myParticle.status(), myParticle.pt(),
	       myParticle.eta(), myParticle.mass(),
	       myParticle.numberOfDaughters());
	for(unsigned index = 0; index < myParticle.numberOfDaughters(); ++index)
	  cout << " " << myParticle.daughter(index)->pdgId();
	cout << endl;
      } 
    }  

      
    //final particles
    if(myParticle.status() == 1) {
      int id = myParticle.pdgId();
      //check if particle of interest
      if(find(_id.begin(),_id.end(),abs(id)) == _id.end()) continue;
      unsigned index = 0;
      for(unsigned i = 0; i < _id.size(); ++i) {
	if(_id[i] == abs(id)) {
	  index = i;
	  break;
	}
      }
      if(myParticle.pt()  > _ptmin[index] &&
	 myParticle.eta() > _etamin[index] &&
	 myParticle.eta() < _etamax[index]) {
	++acceptCount;
	if(_verbose > 1)
	  printf("%4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu (Accepted)\n",
		 particleCount,
		 myParticle.pdgId(), myParticle.status(), myParticle.pt(),
		 myParticle.eta(), myParticle.mass(),
		 myParticle.numberOfDaughters());
      } else if(_ptminloose.size() > 0 && //loose cuts
		myParticle.pt()  > _ptminloose[index] &&
		myParticle.eta() > _etamin[index] &&
		myParticle.eta() < _etamax[index]) {
	++looseCount;
	if(_verbose > 1)
	  printf("%4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu (Loose Accepted)\n",
		 particleCount,
		 myParticle.pdgId(), myParticle.status(), myParticle.pt(),
		 myParticle.eta(), myParticle.mass(),
		 myParticle.numberOfDaughters());
      } else if(_verbose > 2)
	printf("%4u:   %5i,    %2i, %8.2f, %12.2f, %8.2f, %3lu (Rejected)\n",
	       particleCount,
	       myParticle.pdgId(), myParticle.status(), myParticle.pt(),
	       myParticle.eta(), myParticle.mass(),
	       myParticle.numberOfDaughters());
      
    }  
  }
  


  return (acceptCount >= _naccepted || (looseCount+acceptCount >= _naccepted && acceptCount >= _naccepted-_nloose))
	  && (hadTauCount >= _nhadtaus);
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
GenFilter::beginRun(Run&, EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
GenFilter::endRun(Run&, EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
GenFilter::beginLuminosityBlock(LuminosityBlock&, EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
GenFilter::endLuminosityBlock(LuminosityBlock&, EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenFilter::fillDescriptions(ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(GenFilter);

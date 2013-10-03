// -*- C++ -*-
//
// Package:    GenFilter
// Class:      GenFilter
// 
/**\class GenFilter GenFilter.cc GenAnalyzer/GenFilter/src/GenFilter.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
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
};

GenFilter::GenFilter(const ParameterSet& iConfig)
{
    //now do what ever initialization is needed

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

    unsigned leptonCount = 0;

    for (GenParticleCollection::const_iterator iGenPart = genParticleColl->begin(); iGenPart != genParticleColl->end(); ++iGenPart) {
        const GenParticle myParticle = GenParticle(*iGenPart);

        // Look for the ttbar pair
        if (abs(myParticle.pdgId()) == 6 && myParticle.status() == 3) {

            for (unsigned i = 0; i < myParticle.numberOfDaughters(); ++i) {
                const Candidate *ancestor = myParticle.daughter(i);

                // Look for Higgs
                if (abs(ancestor->pdgId()) == 25 && ancestor->status() == 3) {

                    for (unsigned i = 0; i < ancestor->numberOfDaughters(); ++i) {
                        const Candidate *ancestor2 = ancestor->daughter(i);

                        // Looking for Ws
                        if (abs(ancestor2->pdgId()) == 24 && ancestor2->status() == 3) {

                            for (unsigned i = 0; i < ancestor2->numberOfDaughters(); ++i) {
                                const Candidate *ancestor3 = ancestor2->daughter(i);

                                // Looking for leptons from W
                                if (
                                        abs(ancestor3-> pdgId()) == 11 
                                        || abs(ancestor3-> pdgId()) == 13 
                                        || abs(ancestor3-> pdgId()) == 15 
                                   ) {
                                    //cout  << "\t"<< ancestor3->pdgId() << endl;
                                    ++leptonCount;
                                }
                            }
                        }
                    }
                } else if (ancestor->status() == 3) { // Should be Ws and bs

                    // Get the leptons from the W decay
                    if (abs(ancestor->pdgId()) == 24) {

                        for (unsigned i = 0; i < ancestor->numberOfDaughters(); ++i) {
                            const Candidate *ancestor2 = ancestor->daughter(i);

                            // Looking for leptons
                            if (
                                        abs(ancestor2-> pdgId()) == 11 
                                        || abs(ancestor2-> pdgId()) == 13 
                                        || abs(ancestor2-> pdgId()) == 15 
                               ) {
                                //cout  << "\t"<< ancestor2->pdgId() << endl;
                                ++leptonCount;
                            }
                        }
                    } 
                }
            } 
        }
    }

    if (leptonCount > 1) {
        return true;
    } else
        return false;
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

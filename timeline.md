## Project Timeline

### Phase 0: Set Up + Scoping Project (By 28 August)

#### 0.1 Setting Up Splunk DSDL infra
- [X] Set up splunk servers on 2 open net laptops
- [X] Set up splunk dsdl and jupyter lab
- [ ] Replicate environment in home laptop

#### 0.2 Select and ingest datasets
- [ ] Select dataset (current - DARPA cadets dataset)
- [ ] Download and ingest data in all environements
- [ ] Split up the Train and Test Data sets


#### 0.3 Scope project and select use cases
- [X] Identify use case of DSDL (current - Threat Hunting sophisticated attacks)
- [ ] Identify the models to be used (see [here](https://github.com/burdenlife/Splunk-setup/blob/main/models_chosen))
- [ ] Define evaluation rubrics


### Phase 1: Developing PoC (By end September)

#### Phase 1.1 Setting up the Team (by 28 August)
- [ ] Identify team leads
- [ ] Interview team leads and brief
- [ ] Split team members
- [ ] Assign models to teams

#### Phase 1.2 Model Development and Testing 
- [ ] Histogram-Based Outlier Score
- [ ] Isolation Forest
- [ ] Local Outlier Factor
- [ ] One-Class SVM
- [ ] PCA Reconstruction
- [ ] Autoencoder
- [ ] Sequence Model
- [ ] Graph Model

#### Phase 1.3 Reporting and Presentation
- [ ] Creation of Dashboard
- [ ] Presentation Slides
- [ ] Demo of Dashboard
- [ ] Presentation 



### Phase 2: Onboarding models into SOC 

#### Phase 2.1 Retrain with organic data
- [ ] Select model for deployment
- [ ] Extract data from live environment
- [ ] Retrain selected models


#### Phase 2.2 Integrating Model into SOC
- [ ] Place models into SOC environment
- [ ] Update Splunk dashboard to include model query output 
- [ ] Redesign SOPs with respect to new dashboard (retrain cycle, response playbook)
- [ ] Apprise SOC personnel of new SOP




### Phase 3: Evaluation, Assessment and ORD

#### Phase 3.1 Feedback Collection and Dynamic Adjustments
- [ ] Creation of a routine and short-cycle feedback channel
- [ ] Allocation of resources to retrain model according to feedback and latest findings

#### Phase 3.2 ORD
- [ ] Collation of Pilot test data + feedback + lessons learnt
- [ ] Presentation Slides
- [ ] Presentation
- [ ] Potential HOTO or SOP update to maintain stable-state








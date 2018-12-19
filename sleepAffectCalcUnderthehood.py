class processAlg():

    def processAlgIdealDeviation(idealsleeptime,avgweeksleeptime,lastnightsleeptime,mentalComponent,menialComponent,taskTimeUnderIdealSleepConditions):
        #derives relevant variables from three initial points of data
     undersleep=0
     totalweeksundersleeptime=0
     if(idealsleeptime==lastnightsleeptime and idealsleeptime==avgweeksleeptime):
            undersleep=0
            totalweeksundersleeptime=0
     elif(idealsleeptime>lastnightsleeptime):
           undersleep=idealsleeptime-lastnightsleeptime
     elif(idealsleeptime<lastnightsleeptime):
            oversleep=avgweeksleeptime-lastnightsleeptime
     elif(idealsleeptime>avgweeksleeptime):
            totalweeksundersleeptime=((idealsleeptime-avgweeksleeptime)*7)
     elif (idealsleeptime < avgweeksleeptime):
            totalweeksoversleeptime = ((avgweeksleeptime-idealsleeptime) * 7)
     else:print("invalid")

     if (undersleep==0 and totalweeksundersleeptime==0):
           effect=0
     elif (totalweeksundersleeptime<1 or undersleep<.5):
               effect=.10
     elif(totalweeksundersleeptime<2 and undersleep<1):
                    effect= .5
     elif (totalweeksundersleeptime<=6 and undersleep<=3):
                    effect=.75
     else:
                    effect= 1
            #derives the percentage effect on different components of tasks to be used for specific tasks from sleep information

     menialEffect = menialComponent * 8 * effect
     mentalEffect = mentalComponent * 30 * effect
     totaleffectratio=(menialEffect+mentalEffect)/100
            #takes the percentages derived in generalaffectalg and multiplies each percentage affect by it's components percentage composition then adds them together for a final effect ratio
     taskTime= taskTimeUnderIdealSleepConditions+ taskTimeUnderIdealSleepConditions*totaleffectratio
     print(taskTime)
                    # multiplies the ratio obtained in specificAffectAlg by the unmodified task time to obtain current task completion time


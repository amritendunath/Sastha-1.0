
class ForwardChain:
    def _init_(self):
        self.clause_variable_list = ["High blood pressure and progression of disease",
                                                     "Fluid Collection",
                                                     "Inflammation",
                                                     "Poor blood circulation",
                                                     "Narrow blood vessels and chest pain",
                                                     "Elevated Cholesterol",
                                                     "Blood Clotting",
                                                     "Increased Heart Rate",
                                                     "Blockage in blood vessels"]
        self.treatment_list=["ACE INHIBITOR / ARB BLOCKERS",
                                               "DIURETICS / ALDOSTERONE ANTAGONISTS"
                                               "CORTICOSTEROIDS",
                                               "ACE INHIBITOR/ ANGIOTENSIN II RECEPTOR BLOCKERS",
                                               "NITRATES",
                                               "STATIN",
                                               "VAGAL MANEUVER",
                                               "CLOT PREVENTING DRUGS ( CLOPIDOGREL, TICAGRELOR)/ ASPIRIN",
                                               "ANTI-ARRYTHMIC DRUGS",
                                               "NITRATES/ OPEN HEART SURGERY"]                           
        self.diagnosis_list=["Heart Failure", "Cardiomyopathy", "Angina",
                            "Coronary Artery Disease", "Tachycardia", "Ventricular Tachycardia"]
     
        self.diagnosis_ailment = [{0, {0, 1}}, {1, {2, 3}}, {2, {4, 5, 6}}, {3, {0, 6}}, 
                         {4, {6, 7}}, {7, {7, 8}}]
        self.ailment_condition = [
            {"HIGH", "COLLECTED"},
            {"INFLAMED", "REDUCED"},
            {"NARROWED", "ELEVATED", "CLOT"},
            {"HIGH", "CLOT"},{"INCREASED", "CLOT"},
            {"INCREASED", "BLOCKAGE"}]
        self.ailment_condition_treatment = [
            {{self.clause_variable_list[0], "HIGH"}, "ACE-INHIBITOR / ARB BLOCKERS"},
            {{self.clause_variable_list[1], "COLLECTED"}, "DIURETICS / ALDOSTERONE ANTAGONISTS"},
            {{self.clause_variable_list[2], "INFLAMED"}, "CORTICOSTEROIDS"},
            {{self.clause_variable_list[3], "REDUCED"}, "ACE INHIBITOR / ANGIOTENSIN II RECEPTOR BLOCKERS"},
            {{self.clause_variable_list[4], "NARROWED"}, "NITRATES"},
            {{self.clause_variable_list[5], "ELEVATED"}, "STATIN"},
            {{self.clause_variable_list[6], "CLOT"}, "CLOT PREVENTING DRUGS (CLOPIDOGREL, TICAGRELOR) OR ASPIRIN"},
            {{self.clause_variable_list[7], "INCREASED"}, "VAGAL MANEUVER"}]
        
        self.variable_initialized_list = self.variable_initializer(self.clause_variable_list)
        
    # def variable_initializer(variable_list):
    #     temp_var_initializer = []
    #     for variable in variable_list:
    #         temp_pair=(variable, "")
    #         temp_var_initializer.append(temp_pair)
    #     return temp_var_initializer  
    
    # Short form of the above
    def variable_initializer(self, variable_list):
        return [(variable, "") for variable in variable_list]
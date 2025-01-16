class Base:
    def __init__(self):

        # all possible conclusions for our program
        self.conclusions = [
             "Heart Failure", "Cardiomyopathy", "Angina", 
            "Coronary Artery Disease", "Tachycardia", "Ventricular Tachycardia"
        ]

        # variables_list is the list of all symptoms
        self.variables_list = [
            "Rapid/Irregular Heart Beats or Heart Palpitations", "Chest Pain",
            "Persistent Shortness of Breath", "Fatigue", "Dizziness", "Lightheadedness", "Weakness", 
            "Unexplained Sweating", "Fainting", "Weight Gain", "Edema", "Swollen Stomach", "Confusion", 
            "Chest Tightness", "Vomiting", "Restlessness", "Heart Attack", "Nausea", "Tightness in Neck", 
            "Cardiac Arrest", "Lung Congestion"
        ]

        # list of all possible symptoms combination that leads to a diagnosis        
        self.symptoms_combination = [
            [0, 1, 6], [0, 12], [0, 20], [0, 10], [0, 11], [0, 18], [0, 19],
            [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 10], [1, 11], [1, 13],
            [1, 14], [1, 15], [1, 18], [1, 19], [1, 3, 7], [1, 3, 8], [1, 20],
            [1, 5, 6], [1, 5, 7], [1, 5, 9], [1, 12], [1, 6, 9], [1, 6, 7], [1, 6, 8],
            [1, 7], [1, 8, 9], [0, 16], [0, 17], [0, 7], [0, 8, 9], [1, 4, 7], [1, 4, 9]
        ]

        # clauses for diseases, numerical value represents index in the variables list
        self.heart_failure_clause = [0, 1, 3, 4, 6, 8, 9, 12, 20]
        self.cardiomyopathy_clause = [0, 1, 2, 3, 5, 9, 10, 11]
        self.angina_clause = [1, 2, 3, 4, 5, 6, 7, 13, 14, 15]
        self.coronary_clause = [0, 2, 3, 6, 7, 16, 17]
        self.tachycardia_clause = [0, 1, 2, 4, 5]
        self.ventricular_tachycardia_clause = [0, 1, 2, 4, 5, 8, 18, 19]

        # pushing all clauses in the clause index list for easy retrieval later
        self.clause_index = [
            self.heart_failure_clause, 
            self.cardiomyopathy_clause, 
            self.angina_clause, 
            self.coronary_clause, 
            self.tachycardia_clause, 
            self.ventricular_tachycardia_clause
        ]

        self.variable_initialized = self.variable_list_initializer(self.variables_list)
        self.clause_variable_list = self.initialize_clause_variable_list(20, self.clause_index)
    def variable_list_initializer(self, variables_list):
        """
        The variable list initializer function returns a dictionary of variable and their initialization status,
        -1 means the variable has not been initialized, 0 means the variable is false and 1 means the variable is true
        """
        initialized = {variable: -1 for variable in variables_list}
        return initialized

    def initialize_clause_variable_list(self, num_rules, clause_index):
        clause_variable_list = [0] * (num_rules * len(clause_index))
        for i, clause in enumerate(clause_index):
            begin_at = i * num_rules
            for variable_index in clause:
                clause_variable_list[begin_at + variable_index] = 1
        return clause_variable_list
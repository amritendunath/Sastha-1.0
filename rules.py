import base as b
import forward_rules as fr

class Rules:
    def __init__(self):
        self.final_diagnosis = ""

        # Rule numbers
        self.rule_number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

        # Diagnosis index
        self.diagnosis_index = [0, 0, 0, 1, 1, 5, 5, 2, 2, 5, 1, 1, 1, 2, 2, 2, 5, 5, 2, 0, 0, 2, 2, 1, 0, 0, 2, 0, 2, 0, 3, 3, 3, 3, 2, 0]

        # Symptoms combination
        self.symptoms_combination = [
            [0, 1, 6], [0, 12], [0, 20], [0, 10], [0, 11], [0, 18], [0, 19],
            [1, 2, 6], [1, 2, 7], [1, 2, 8], [1, 2, 9], [1, 10], [1, 11],
            [1, 13], [1, 14], [1, 15], [1, 18], [1, 19], [1, 3, 7], [1, 3, 8],
            [1, 20], [1, 5, 6], [1, 5, 7], [1, 5, 9], [1, 12], [1, 6, 9],
            [1, 6, 7], [1, 6, 8], [1, 7], [1, 8, 9], [0, 16], [0, 17], [0, 7],
            [0, 8, 9], [1, 4, 7], [1, 4, 9]
        ]

        # Initialize rule_symptoms map
        self.rule_symptoms = self.initialize_rule_symptoms(self.rule_number, self.symptoms_combination)

        # Initialize conclusion list
        self.conclusion_list = self.initialize_conclusion_list(36)

        # Visited conclusion list
        self.visited_conclusion_list = []

        # Conclusion stack
        self.conclusion_stack = self.initialize_stack()

        # Initialize a knowledge_base object
        self.current_knowledge = b.Base()          

    def initialize_stack(self):
        conclusion_stack = [(10, 0)]
        return conclusion_stack 
    
    def initialize_conclusion_list(self, num_rules):
        rules_conclusions = [(i, "diagnosis") for i in range(1, num_rules + 1)]
        return rules_conclusions
    
    def initialize_rule_symptoms(self, rules, symptoms):
        if len(rules) != len(symptoms):
            print("Rules and symptoms size mismatch. Recheck data.")
            return {}

        rule_symptoms = {rules[i]: symptoms[i] for i in range(len(rules))}
        return rule_symptoms    
    def check_conclusion_stack(self):
        if not self.conclusion_stack:
            self.conclusion_stack.append((10,0))
        return self.conclusion_stack[-1]
    
    def start_iteration(self):
        response = ""
        response_value = 0

        rule_to_process = self.check_conclusion_stack()
        variable_index = rule_to_process[1]

        while response not in ["Y", "N", "y", "n"]:
            condition = self.current_knowledge.variables_list[variable_index]
            response = input(f"Does the patient have {condition}? enter: Y/N\n")

        response_value = 1 if response in ["Y", "y"] else 0
        self.update_response(response_value, variable_index)

    def update_response(self, variable_value, variable_position):
        self.current_knowledge.variable_initialized[self.current_knowledge.variables_list[variable_position]] = variable_value
        rule_to_process = self.check_conclusion_stack()
        rule_num_to_process = rule_to_process[0]
        self.process_response(rule_num_to_process)

    def process_response(self, rule_num_to_process):
        next_rule = -1
        symptoms_for_rule = self.rule_symptoms[rule_num_to_process]
        for symptom in symptoms_for_rule:
            if self.current_knowledge.variable_initialized[self.current_knowledge.variables_list[symptom]] == 0:
                self.visited_conclusion_list.append((rule_num_to_process, "diagnosis"))
                self.conclusion_stack.pop()
                next_rule = rule_num_to_process + 10

                if next_rule > self.rule_number[-1]:
                    print("Diagnosis not possible at this time. Please refer to an MD.")
                    self.end_program()
                    return
                
                next_set_of_symptom = self.rule_symptoms[next_rule]
                self.conclusion_stack.append((next_rule, next_set_of_symptom[0]))
                self.process_response(next_rule)
                return

            elif self.current_knowledge.variable_initialized[self.current_knowledge.variables_list[symptom]] == -1:
                next_rule = rule_num_to_process
                self.conclusion_stack.pop()
                self.conclusion_stack.append((next_rule, symptom))
                self.start_iteration()
                return
            
        if next_rule == -1:
            print("\n\nThe patient is showing the following symptoms:\n\n")
            for each_symptom in self.rule_symptoms[rule_num_to_process]:
                symptom_description = self.current_knowledge.variables_list[each_symptom]
                print(symptom_description)

            self.final_diagnosis = self.current_knowledge.conclusions[self.diagnosis_index[(rule_num_to_process // 10) - 1]]
            print(f"\n\nThe patient might be suffering from {self.final_diagnosis}. Please perform appropriate tests to confirm and treat for the condition.\n\n")
            self.end_program()

    def end_program(self):
        treatment = fr.ForwardRules(self.get_diagnosis())
        if self.get_diagnosis() == "":
            treatment.end_program()
        else:
            treatment.initialize_forward_rule()        

    def get_diagnosis(self):
        return self.final_diagnosis
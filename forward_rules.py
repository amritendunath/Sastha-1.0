from queue import Queue
import forward_base as kb

class ForwardChain:
    def __init__(self):
        self.diagnosis_list = kb.ForwardChain.diagnosis_list
        self.diagnosis_ailment = kb.ForwardChain.diagnosis_ailment
        self.ailment_condition = kb.ForwardChain.ailment_condition
        self.ailment_condition_treatment = kb.ForwardChain.ailment_condition_treatment
        self.variable_initialized_list = kb.ForwardChain.variable_initialized_list


class ForwardRules:     
        def _init_(self, diagnosis):
             self.diagnosis= diagnosis
             self.variable_initialized_queue= Queue()
             self.chain_forward = kb.ForwardChain
        
        def initialize_ailment(self, diagnosis_index):
            for diagnosis_ailment_pair in self.chain_forward.diagnosis_ailment:
                if diagnosis_index == diagnosis_ailment_pair[0]:
                    ailment_index = diagnosis_ailment_pair[1]

                for ailment_number in ailment_index:
                    variable_initialized=  list(self.chain_forward.variable_initialized_list[ailment_number])
                    variable_initialized[1]= self.chain_forward.ailment_condition[diagnosis_index][ailment_number]
                    self.chain_forward.variable_initialized_list[ailment_number] = tuple(variable_initialized)
                    self.variable_initialized_queue.put(self.chain_forward.variable_initialized_list[ailment_number])
            self.apply_forward_chain()


        def apply_forward_chain(self):
            while not self.variable_initialized_queue.empty():
                varible = self.variable_initialized_queue.get()       

                for ailment_condition_treat in self.chain_forward.ailment_condition_treatment:
                    ailment_condition = ailment_condition_treat[0]

                    if varible[0] == ailment_condition[0]:
                        output_print = f"\n\nThe patient might have {varible[0]}"
                        treatment_print = f"\n Treat {varible[0]} with {ailment_condition_treat[1]}"

                        print(output_print)
                        print(treatment_print)

        def end_program(self):
            print("\n\n\n\nThank you for using this program!")
            exit(0)
        
        def initialize_forward_rule(self):
            diagnosis_index = 0
            for i, diagnosis_index in enumerate(self.chain_forward.diagnosis_list):
                if diagnosis_index == self.diagnosis:
                    diagnosis_index = i
                    break
            self.initialize_ailment(diagnosis_index)
            self.end_program()  
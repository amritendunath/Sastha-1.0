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
                            



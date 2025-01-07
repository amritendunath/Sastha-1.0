from queue import Queue
import forward_base as kb

class ForwardChain:
    def __init__(self):
        self.diagnosis_list = kb.ForwardChain.diagnosis_list
        self.diagnosis_ailment = kb.ForwardChain.diagnosis_ailment
        self.ailment_condition = kb.ForwardChain.ailment_condition
        self.ailment_condition_treatment = kb.ForwardChain.ailment_condition_treatment
        self.variable_initialized_list = kb.ForwardChain.variable_initialized_list


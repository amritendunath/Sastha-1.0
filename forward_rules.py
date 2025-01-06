from queue import Queue
import forward_base as kb

class ForwardChain:
    def __init__(self):
        self.diagnosis_ailment = kb.ForwardChain.diagnosis_ailment
        self.variable_initialized_list = kb.ForwardChain.variable_initialized_list
        self.ailment_condition = kb.ForwardChain.ailment_condition
        self.ailment_condition_treatment = kb.ForwardChain.ailment_condition_treatment
        self.diagnosis_list = kb.ForwardChain.diagnosis_list
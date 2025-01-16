# An implementation of backward chaining and forward chaining in creating an
# expert system for a hospital in diagnosing cardiovascular diseases and to
# recommend treatment based on the diagnosis.
import rules as fr
class Rules:
    def __init__(self):
        pass

    def start_iteration(self):
        # Placeholder for the logic to start the diagnosis iteration
        print("Starting diagnosis iteration...")

def main():
    print("Welcome to the Diagnosis-Treatment program for Heart Diseases!\n\n\n")
    
    heart_disease_diagnosis = fr.Rules()
    heart_disease_diagnosis.start_iteration()

if __name__ == "__main__":
    main()
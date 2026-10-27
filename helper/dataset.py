from datasets import load_dataset 

class MIRACLDataset():
    def load_train(self):
        return load_dataset("miracl/miracl-corpus", "id", split="train", trust_remote_code=True)

    def load_dev(self):
        return load_dataset("miracl/miracl", "id", trust_remote_code=True)['dev']
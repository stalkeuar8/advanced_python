class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        print("Analysing data...\nReport ready!")
        return self.data
    
class PrintReport:
   
   def print_report(self, report):
        print(f"Printing to console: {report}")
    

class SaveToFile:

    def save_to_file(self, filename, report):
        with open(filename, "w") as f:
            # f.write(report)
            pass
        print(f"Saved to {filename}")


report = Report("fsdfsdfsdfsf")
PrintReport().print_report(report.data)
SaveToFile().save_to_file('somefile', report.data)
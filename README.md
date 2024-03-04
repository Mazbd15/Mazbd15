class RubricItem:
    def __init__(self, description, fulfilled=False):
        self.description = description
        self.fulfilled = fulfilled

class Rubric:
    def __init__(self):
        self.items = {
            1: RubricItem("Delayed Dataset Selection: Utilized the same assigned dataset."),
            2: RubricItem("Problem/Task Objectives/Goals: Well-motivated, interesting, insightful, and novel"),
            3: RubricItem("Selection of the Data: Data have 10-20 mixed variables and more than 300 samples."),
            4: RubricItem("Listing and Identification of the Variables: The description and type of variables are well reported."),
            5: RubricItem("List Inconsistencies, Missing Data, and Outliers: Inconsistencies, missing data, and outliers are reported, and appropriate tools are adopted to fix these issues."),
            6: RubricItem("Statistical Summary: The statistical summary is well provided for both numeric and categorical variables."),
            7: RubricItem("Graphics: Plots convey information correctly with adequate and appropriate information, and all varieties of plots (Univariate, Bivariate, and advanced) are considered."),
            8: RubricItem("Relationship Correlation: Correlation is reported, and results are well-concluded."),
            9: RubricItem("Data Analysis and Model Selection: Analysis/model is appropriate, complete, advanced, and informative (Multiple appropriate models or alternative models are used)."),
            10: RubricItem("Validation of Model: Did validation analysis and chose the final model on the best parameters."),
            11: RubricItem("Interpretation of Analysis: Relevant interpretation on unscaled data, is explicitly tied to analysis and context."),
            12: RubricItem("Operationalize: Provided problems and notes on implementation in full detail."),
            13: RubricItem("Results/Conclusion: Relevant conclusions are explicitly tied to analysis and context. Key findings are well communicated."),
            14: RubricItem("Project Consistency: All the project parts are consistent and well-integrated."),
            15: RubricItem("Teamwork: The team demonstrates exceptional collaboration and communication within the team and with the instructor. Contributions from all team members are evident and clearly observed by the instructor.")
        }

    def evaluate(self):
        for item_num, item in self.items.items():
            print(f"{item_num}: {item.description} - {'Fulfilled' if item.fulfilled else 'Not Fulfilled'}")

# Create an instance of the Rubric class
rubric = Rubric()

# Update rubric items based on evaluation
# For example:
rubric.items[1].fulfilled = True
rubric.items[2].fulfilled = True
rubric.items[3].fulfilled = True
# Continue updating other items...

# Evaluate and print the rubric
rubric.evaluate()

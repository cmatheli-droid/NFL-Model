
# NFL MVP Ladder

**Group Name:** Group 5 

**Team Members:** Chelsea Mathelier, Sai Bevara, Opie Opie, Aishwarya Kompella

## Project Overview

The NFL MVP Ladder is a machine learning project designed to analyze NFL player statistics and estimate which players may be strong candidates for the Most Valuable Player (MVP) award.

The project uses data from the SportsDataIO NFL API and Python to prepare player statistics for machine learning. The goal is to explore how player performance relates to MVP voting while examining potential bias, especially the historical preference for quarterbacks. The tool is also a way to provide a more user friendly interface, which can make predictions and the MVP ladder easier to understand. Creating an NFL MVP prediction machine that evaluates players across every position will hopefully bring the benefit of eliminating QB bias in MVP races in the NFL. In the last ten years, all NFL MVPs have all been quarterbacks. The goal of our model is to eliminate QB bias and bring a broader research field for all positions.Also, our model will help relay transparency. Even outside of the QB position, people can be biased; they can be biased toward a certain player who is loved inside the NFL.


## Technologies Used

- Python
- Pandas
- Requests
- Scikit-learn
- AWS S3
- SportsDataIO NFL API

## Installation

Install Python 3.10 or later, then install the required libraries:

```bash
python -m pip install pandas requests scikit-learn boto3
```

## API Configuration

Obtain an API key from SportsDataIO and set it as an environment variable.

macOS/Linux:

```bash
export SPORTSDATA_API_KEY="your_api_key_here"
```

Never upload your API key or AWS credentials to GitHub.

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/cmatheli-droid/NFL-Model.git
cd NFL-Model
```

2. Install the required libraries using the command above.
3. Configure your SportsDataIO API key.
4. Add and run the project's data ingestion and model training code.

**Note:** A runnable demo script and sample dataset will be added to the repository. Update this section with the exact command once the demo is implemented.

## Installation

Install the required libraries:

```bash
python -m pip install pandas scikit-learn
```

## Run the demonstration

From the root directory of the repository, run:

```bash
python bin/train_demo.py
```

The script trains a small example classifier and prints a demonstration MVP probability. It uses fictional sample data and is not the final NFL MVP model.

## Project Workflow

1. Retrieve NFL player statistics through the SportsDataIO API.
2. Clean and prepare the data using Pandas.
3. Select relevant player performance features.
4. Train and evaluate a machine learning model using Scikit-learn.
5. Generate player rankings or MVP predictions.
6. Evaluate possible bias across player positions.

## Main Functions

The following functions describe the planned workflow. Update and match their names to match the implemented code.

- `fetch_player_stats()`: Retrieves NFL player statistics from the API.
- `prepare_features()`: Cleans the data and selects relevant model features.
- `save_processed_data()`: Saves processed data locally or to AWS S3.
- `train_model()`: Trains the machine learning model on historical data.
- `predict_mvp_candidates()`: Generates predictions or rankings for MVP candidates.
- `evaluate_model()`: Measures model performance and helps identify limitations.

## Data Features

Potential features include passing yards, passing touchdowns, interceptions, rushing yards, rushing touchdowns, receiving yards, receiving touchdowns, games played, and team performance. Our model aims to compare players across different positions using position-specific statistics. This allows users to see how players at positions such as wide receiver and running back compare to quarterbacks. The tool provides a user-friendly interface that makes MVP ladders and predictions easy to understand. So using multiple but impactful data features is important here to try to eliminate bias.


The final features will depend on the available API data and the implemented model.

## Bias and Fairness

Historical MVP voting may favor certain positions, particularly quarterbacks. The project will examine whether model predictions unequally favor particular positions and explore ways to evaluate player performance more fairly.

## Limitations

Predictions are estimates, not guarantees of who will win MVP. Historical voting patterns, missing data, and differences between player positions may affect model results. We may still end with a prediction that doesn't have bias however it might favor the historical data.

## Questions and Contact

**Contact:** cmatheli@charlotte.edu, sbevara@charlotte.edu, gopie@charlotte.edu, akompel1@charlotte.edu
For questions or issues, use the GitHub Issues page:
https://github.com/cmatheli-droid/NFL-Model/issues

## License

See the [LICENSE](LICENSE) file for licensing information.

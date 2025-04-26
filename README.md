# Analysis-of-vaccination-status-in-the-United-States-12-months-after-the-start-of-covid19
This project explored Covid-19 vaccine distribution data in the United States from 12/21/2020 - 4/12/2021.

## Project Summary: COVID-19 Vaccine Distribution Analysis by U.S. State (Moderna)

### 1. Problem Statement and Objective:
This project focuses on analyzing the distribution of the Moderna COVID-19 vaccine across different U.S. states during the pandemic. Moderna vaccines were distributed weekly starting from December 2020. The project's objectives were:
- To determine how many Moderna vaccine doses each state received from December 21, 2020, to April 12, 2021.
- To identify which states received the largest total number of vaccine doses.

### 2. Data Source and Description:
- **Data Source**: CDC official vaccine distribution dataset (COVID-19 Vaccine Distribution Allocations by Jurisdiction – Moderna).
- **Data Structure**: CSV file with four columns:
  - State Name
  - Date of Vaccine Allocation
  - First Dose Quantity
  - Second Dose Quantity

### 3. Research Methods:
The project utilized Python programming and included the following methods:

- **Data Import and Preprocessing**:
  - Custom-built functions (`read_csv()` and `get_col()`) for reading CSV files and extracting specific columns.

- **Data Aggregation and Statistical Analysis**:
  - Created a dictionary (`vaccine_by_state()`) mapping each state to its list of vaccine allocation quantities.
  - Used the `count_categories()` function to calculate total vaccines distributed per state.

- **Identifying Key Metrics**:
  - Employed the `max_vaccines()` function to determine the state with the highest vaccine distribution.

### 4. Data Visualization:
- Three main types of visualizations were created using `matplotlib`:
  - **Bar Charts**: Displayed total vaccine allocations per state, presented both alphabetically and sorted by vaccine quantities.
  - **Pie Chart**: Highlighted the proportion of vaccine distributions for the top ten states.
- An attempt was made to create geographical visualizations using Cartopy maps, but the implementation was unsuccessful due to technical challenges.

### 5. Key Findings:
- California received the most vaccine doses (approximately 5.99 million first doses), followed by Texas (around 4.10 million doses) and Florida (about 3.28 million doses).
- Despite higher COVID-19 infection rates, New York state received significantly fewer doses (1.75 million) compared to California and Texas.
- Data was available for only 38 states, with missing states possibly utilizing other vaccine brands (such as Pfizer or Johnson & Johnson) or having quantities too small to report.

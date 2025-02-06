#  DocNet: Semantic Structure in Inductive Bias Detection Models
This repository holds the raw partisan topic data and cleaned code used in the 17th ACM Web Science Conference 2025 submission "DocNet: Semantic Structure in Inductive Bias Detection Models"

For the BASIL dataset see: https://github.com/launchnlp/BASIL

## Contents
* data/\*.pkl: news articles for each topic
* data/datasheet.md: Background on data
* inductive_pipeline.py  and inductive_pipeline_basil.py: pipeline for experimenting across embedding configurations
* Document-level Bias by LLM.ipynb: notebook for LLM bias detection
* process_data.py: functions for cleaning the data
* newsnet_utils.py: functions for creating the document networks
* analysis_utils.py: functions for varying embedding configurations
* run_gcngae.py: functions for creatting autoencoder models (with GCN encoder)

## Usage
1. Clean the data using `process_data.py`
2. Update scripts/notebooks with processed data file paths
2. Train desired model or full experimental configuration using the respective `run_{insert modelname}` functions or run `inductive_pipeline.py` as main

## License
This source code is licensed under MIT License and the data files are licensed under CC0 1.0 Universal. 

## Citation
Cite the following if you use the partisan topic dataset or our code:

Jessica Zhu, Michel Cukier, and Iain Cruickshank. 2025. DocNet: Semantic
Structure in Inductive Bias Detection Models. In Proceedings of ACM Web
Science Conference (WEBSCI ’25). ACM, New York, NY, USA, 10 pages. https:
//doi.org/XXXXXXX.XXXXXXX

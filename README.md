# **SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models**

Shyam Sundar Kannan, Vishnunandan L. N. Venkatesh, and Byung-Cheol Min. 

Submitted to IEEE International Conference on Robotics and Automation (ICRA ), 2024

[Project Page](https://sites.google.com/view/smart-llm/) | [arXiv](https://arxiv.org/abs/2309.10062) | [Video](https://www.youtube.com/watch?v=mssTPl7ifyI)

**Abstract:** In this work, we introduce SMART-LLM, an innovative framework designed for embodied multi-robot task planning. SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (LLMs), harnesses the power of LLMs to convert high-level task instructions provided as input into a multi-robot task plan. It accomplishes this by executing a series of stages, including task decomposition, coalition formation, and task allocation, all guided by programmatic LLM prompts within the few-shot prompting paradigm. We create a benchmark dataset designed for validating the multi-robot task planning problem, encompassing four distinct categories of high-level instructions that vary in task complexity. Our evaluation experiments span both simulation and real-world scenarios, demonstrating that the proposed model can achieve promising results for generating multi-robot task plans.

## Setup
Create a conda environment (or virtualenv):
```
conda create -n smartllm python==3.9
```

Install dependencies:
```
pip install -r requirments.txt
```

## Creating OpenAI API Key
The code relies on OpenAI API. Create an API Key at https://platform.openai.com/.

Create a file named ```api_key.txt``` in the root folder of the project and paste your OpenAI Key in the file. 

## Running Script
Run the following command to generate output execuate python scripts to perform the tasks in the given AI2Thor floor plans. 

Refer to https://ai2thor.allenai.org/demo for the layout of various AI2Thor floor plans.
```
python3 scripts/run_llm.py --floor-plan {floor_plan_no}
```
Note: Refer to the script for running it on different versions of GPT models and changing the test dataset. 

The above script should generate the executable code and store it in the ```logs``` folder.


Run the following script to execute the above generated scripts and execute it in an AI2THOR environment. 

The script requires command which needs to be executed as parameter. ```command``` needs to be the folder name in the ```logs``` folder where the executable plans generated are stored. 
```
python3 scripts/execute_plan.py --command {command}
```
## Dataset
The repository contains numerous commands and robots with various skill sets to perform heterogenous robot tasks. 

Refer to ```data\final_test\``` for the various tasks, robots available for the tasks, and the final state of the environment after the task for evaluation. 

The file name corresponds to the AI2THOR floor plans where the task will be executed. 

Refer to ```resources\robots.py``` for the list of robots used in the final test and the skills possessed by each robot. 


## Citation
If you find this work useful for your research, please consider citing:
```
@article{kannan2023smart,
    title={SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models},
  	author={Kannan, Shyam Sundar and Venkatesh, Vishnunandan LN and Min, Byung-Cheol},
  	journal={arXiv preprint arXiv:2309.10062},
 	year={2023}
}
```

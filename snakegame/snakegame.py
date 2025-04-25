import autogen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

def main():

    # load configuration from json file
    # It should include the information of used LLM
    config_list = config_list_from_json(
        env_or_file = "OAI_CONFIG_LIST.json",
    )

    # This the object that agent need for configuring its LLM
    llm_config = {
        "cache_seed" : 46,       # used to store different chat, used as a id
        "temperature" : 0,
        "config_list" : config_list,
        "timeout": 120
    }

    # Create the agents
    user_agent = UserProxyAgent(
        name = "Admin",
        system_message = "You are a user agent. You are responsible for runing the code to test whether the code is running successfully.",
        human_input_mode="NEVER",
        code_execution_config = {
            "work_dir": "game",
            "use_docker": False, 
        }
    )

    EngineerAgent = AssistantAgent(
        name = "engineer",
        llm_config = llm_config,
        system_message = """You are a software engineer. You follow a approved plan. Please write python or sh code to solve tasks.
        remember to put # filename: <filename> inside the code block
        """,
    )

    PlannerAgent = AssistantAgent(
        name = "planner",
        llm_config = llm_config,
        system_message = """You are a planner agent. You will create a plan to solve the task.
        You will break the task into smaller subtasks and give the specific instructions to the engineer agent.
        """,
    )

    CriticAgent = AssistantAgent(
        name = "critic",
        llm_config = llm_config,
        system_message = """You are a critic agent. You will review the plan and codes. Give feedback to other agent to revise plan or code.
        Focus on the logic sequence of the plan and the details of the tasks.
        """,
    )

    groupchat = autogen.GroupChat(
        agents = [user_agent, EngineerAgent, PlannerAgent, CriticAgent],
        messages = [],
        max_round = 20
    )

    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Start the group chat
    user_agent.initiate_chat(
        manager,
        message = "I want to create a snake game using pygame. Can you help me with that?",
    )

if __name__ == "__main__":
    main()





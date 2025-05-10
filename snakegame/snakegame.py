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
        "cache_seed" : 53,       # used to store different chat, used as a id
        "temperature" : 0,
        "config_list" : config_list,
        "timeout": 120
    }

    # Create the agents
    user_agent = UserProxyAgent(
        name = "Executor",
        system_message = "Executor, Execute the code written by the engineer and suggest updates if any error showed.",
        human_input_mode="NEVER",
        code_execution_config = {
            "last_n_messages" : 3,
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
        system_message = """You are a planner agent.Given the task you should give out a plan on just coding. But you don't need to write codes""",
    )

    groupchat = autogen.GroupChat(
        agents = [user_agent, EngineerAgent, PlannerAgent],
        messages = [],
        max_round = 7
    )

    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Start the group chat
    user_agent.initiate_chat(
        manager,
        message = """I want to create a snake game using pygame. Can you help me with that? 
        The game broad should be 20 x 20 in grid. and the snake should be able to eat  the food and grow consequently. The game should be playable using arrow keys. The snake should be able""",
    )

if __name__ == "__main__":
    main()





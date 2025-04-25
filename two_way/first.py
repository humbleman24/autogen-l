from autogen import UserProxyAgent, AssistantAgent, config_list_from_json

def main():
    config_list = config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )

    llm_config = {"config_list":config_list}

    User = UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config={
            "use_docker":False,
            "work_dir": "plot_dir"
        }
    )

    Assistant = AssistantAgent(
        name="assistant",
        llm_config=llm_config
    )

    User.initiate_chat(Assistant, message="Plot and save the chat of NVIDIA and TESLA stock price change.")


if __name__ == "__main__":
    main()
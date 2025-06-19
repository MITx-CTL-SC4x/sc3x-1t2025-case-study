APP_URL = "URL"
#APP_IMAGE = "debate_flat.webp"
PUBLISHED = True

# APP_TITLE = "Title"
# APP_INTRO = """
# Intro
# """
# APP_HOW_IT_WORKS = """
#  How it Works
#  """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """
You are a global supply chain expert guiding a supply chain executive through short-term responses to a 25 percent import tariff. The background on the company and scenario are:
The toy industry is deeply affected by tariffs, making it a compelling case study. A strong example is Mattel, the multinational toy company behind Barbie, Hot Wheels, and Fisher-Price. Mattel has a global supply chain, with significant production in China, where about 80 percent of U.S. toy imports originate.
Short-Term Challenges
Rising Costs: Tariffs on Chinese imports have forced Mattel to increase toy prices, impacting affordability for consumers.
Supply Chain Adjustments: The company is reducing reliance on China, shifting production to India and Vietnam, which offer lower labor costs.
Retail Disruptions: Higher costs may lead to lower inventory levels at major retailers, affecting holiday sales.
Long-Term Challenges
Strategic Manufacturing Shifts: Mattel aims to cut Chinese production below 40 percent by 2025, but transitioning supply chains is complex.
Global Trade Uncertainty: Future tariff policies could further disrupt sourcing strategies, requiring continuous adaptation.
Consumer Behavior Changes: Higher prices may shift demand toward alternative brands or second-hand markets.
This case study allows students to explore import/export implications, cost management, and strategic responses to trade policies. 
Do not mention Mattel or the toy industry explicitly, as they were mentioned for ilustrative purposes only.
"""

PHASES = {
    "name": {
        "name": "What is your first name?",
        "fields": {
            "name": {
                "type": "text_input",
                "key": "name",
                "label": """What is your first name?""",
                "value": "",
            }
        },
        "phase_instructions": "The user will provide you their name. In one sentence only, welcome them by name and end your statement with 'Let's discuss responses to the short-term impacts of a 25 percent tariff.'",
        "user_prompt": "My name is {name}",
        "ai_response": True,
        "scored_phase": False,
        "minimum_score": 2,
        "rubric": """  """,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic1select": { # TOPIC 1
        "name": "Choose a Topic to Discuss",
        "fields": {
            "topic": {
                "type": "selectbox",
                "key": "topic1select",
                "label": "Topic 1: Choose a topic to discuss first",
                "options": ['Inventory - Should we build buffer stock or reduce exposure?', 'Logistics - Are there alternatives to speed or reroute shipments?', 'Suppliers - Should we shift or renegotiate sourcing in the near term?', 'Customers - How should we handle pricing and communication?']
            }
        },
        "phase_instructions": "Once they choose a topic, ask a short open-ended question focused on that topic. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Keep track which topics have been completed.",
        "user_prompt": "{topic}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic1follow1": {
        "name": "Topic 1: Respond to the comments above",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow1",
                "height": 300,
                "label": """Topic 1: Respond to the comments above""",
                "value": """ respond_to_topic_1_first_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a second open-ended question on the topic that builds on the previous discussion but explores new ideas.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic1follow2": {
        "name": "Topic 1, Second Question",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow2",
                "height": 300,
                "label": """Topic 1: Respond to the comments above""",
                "value": """ respond_to_topic_1_second_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the second open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a third open-ended question on the topic that builds on the previous discussion but explores new ideas.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic1follow3": {
        "name": "Topic 1, Third Question",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow3",
                "height": 300,
                "label": """Topic 1: Respond to the comments above""",
                "value": """ respond_to_topic_1_third_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the third open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by suggesting they choose a new topic they have not discussed yet.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic2select": { # TOPIC 2
        "name": "Choose a Second Topic",
        "fields": {
            "topic": {
                "type": "selectbox",
                "key": "topic2select",
                "label": "Topic 2: Choose a new topic you have not already discussed",
                "options": ['Inventory - Should we build buffer stock or reduce exposure?', 'Logistics - Are there alternatives to speed or reroute shipments?', 'Suppliers - Should we shift or renegotiate sourcing in the near term?', 'Customers - How should we handle pricing and communication?']
            }
        },
        "phase_instructions": "Once they choose a new topic, ask an open-ended question focused on the new topic. Gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Keep track which topics have been completed.",
        "user_prompt": "{topic}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic2follow1": {
        "name": "Topic 2, First Question",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow1",
                "height": 300,
                "label": """Topic 2: Respond to the comments above""",
                "value": """ respond_to_topic_2_first_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a second open-ended question on the topic that builds on the previous discussion but explores new ideas.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic2follow2": {
        "name": "Topic 2, Second Question",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow2",
                "height": 300,
                "label": """Topic 2: Respond to the comments above""",
                "value": """ respond_to_topic_2_second_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the second open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a third open-ended question on the topic that builds on the previous discussion but explores new ideas.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "topic2follow3": {
        "name": "Topic 2, Third Question",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow3",
                "height": 300,
                "label": """Topic 2: Respond to the comments above""",
                "value": """ respond_to_topic_2_third_question_here """,
            }
        },
        "phase_instructions": "The user will respond to the third open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by suggesting they choose a new topic they have not discussed yet.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "plan": {
        "name": "Mitigation Plan",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "plan",
                "height": 300,
                "label": """Please describe your mitigation plan""",
                "value": """ describe_migitation_plan_here """,
            }
        },
        "phase_instructions": "The user will respond with a summary of their short-term mitigation plan. It should be concise and executive-ready. Provide brief constructive feedback on their plan. Finish by thanking them for the discussion.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    }
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = False
DISPLAY_COST = False

COMPLETION_MESSAGE = "You've reached the end!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "SC3x 1T2025, Case Study, Short-term Impact Discussion",
    #"page_icon": "🗣️️",
    "layout": "centered",
    #"initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())

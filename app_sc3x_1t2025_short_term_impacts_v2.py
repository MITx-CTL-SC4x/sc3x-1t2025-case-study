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
You are a global supply chain expert guiding a supply chain executive through short-term responses to a 25 percent import tariff.

Below is an example company and scenario to provide context for the discussion of import/export implications, cost management, and strategic responses to trade policies.

The toy industry is deeply affected by tariffs, making it a compelling case study. A strong example is Mattel, the multinational toy company behind Barbie, Hot Wheels, and Fisher-Price. Mattel has a global supply chain, with significant production in China, where about 80 percent of U.S. toy imports originate.

Short-Term Challenges:
- Rising Costs: Tariffs on Chinese imports have forced Mattel to increase toy prices, impacting affordability for consumers.
- Supply Chain Adjustments: The company is reducing reliance on China, shifting production to India and Vietnam, which offer lower labor costs.
- Retail Disruptions: Higher costs may lead to lower inventory levels at major retailers, affecting holiday sales.

Long-Term Challenges:
- Strategic Manufacturing Shifts: Mattel aims to cut Chinese production below 40 percent by 2025, but transitioning supply chains is complex.
- Global Trade Uncertainty: Future tariff policies could further disrupt sourcing strategies, requiring continuous adaptation.
- Consumer Behavior Changes: Higher prices may shift demand toward alternative brands or second-hand markets.

The executive you will have a discussion with received the email below from the CEO of their company.

From: CEO
Subject: URGENT - Tariff Impact Assessment

We've just learned that a 25% tariff will immediately apply to a critical imported component. I need you to lead our short-term response.

I need a rapid assessment of the pros, cons, and implications of:
1. Inventory - Should we build buffer stock or reduce exposure?
2. Logistics - Are there alternatives to speed or reroute shipments?
3. Suppliers - Should we shift or renegotiate sourcing in the near term?
4. Customers - How should we handle pricing and communication?

I expect a full mitigation plan by Friday. Please explore each area carefully, then come back to me with a concise action plan.

—CEO

Your role is to guide the executive through a structured discussion. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Gently challenge their thinking. Do not focus on the company Mattel or the toy industry explicitly, as they are mentioned here for ilustrative purposes only.
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
        "phase_instructions": "The user will provide you their name. In one sentence only, welcome them by name and end your statement with 'Let's discuss responses to the short-term impacts of a 25 percent tariff.' Then invite them to choose one of the four topics to discuss.",
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
                "label": "Choose the first topic to discuss:",
                "options": ['Inventory - Should we build buffer stock or reduce exposure?', 'Logistics - Are there alternatives to speed or reroute shipments?', 'Suppliers - Should we shift or renegotiate sourcing in the near term?', 'Customers - How should we handle pricing and communication?']
            }
        },
        "phase_instructions": "Once they choose a topic, ask a short open-ended question focused on that topic that prompts them to think about the topic without too much effort. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Do not provide an explanation of the topic. Instead, provide a brief description of an example relevant for the topic and to help provide context for the discussion. Keep track which topics have been completed.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow1",
                "height": 300,
                "label": """Response:""",
                "value": """What are your initial thoughts on the topic?""",
            }
        },
        "phase_instructions": "The user will respond to the open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a second open-ended question on the topic that builds on the previous discussion but explores new ideas. Provide context for the new question by building on the example you previous introduced for the topic.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow2",
                "height": 300,
                "label": """Response:""",
                "value": """Please share your thoughts on the feedback above""",
            }
        },
        "phase_instructions": "The user will respond to the second open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a third open-ended question on the topic that builds on the previous discussion but explores new ideas. Provide context for the new question by building on the example you previous introduced for the topic.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic1follow3",
                "height": 300,
                "label": """Response:""",
                "value": """Please respond considering the discussion above""",
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
                "label": "Choose a new topic you have not already discussed:",
                "options": ['Inventory - Should we build buffer stock or reduce exposure?', 'Logistics - Are there alternatives to speed or reroute shipments?', 'Suppliers - Should we shift or renegotiate sourcing in the near term?', 'Customers - How should we handle pricing and communication?']
            }
        },
        "phase_instructions": "Once they choose a new topic, ask a short open-ended question focused on that topic that prompts them to think about the topic without too much effort. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Do not provide an explanation of the topic. Instead, provide a brief description of an example relevant for the topic and to help provide context for the discussion. Keep track which topics have been completed.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow1",
                "height": 300,
                "label": """Response:""",
                "value": """What are your initial thoughts on the new topic?""",
            }
        },
        "phase_instructions": "The user will respond to the open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a second open-ended question on the topic that builds on the previous discussion but explores new ideas. Provide context for the new question by building on the example you previous introduced for the topic.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow2",
                "height": 300,
                "label": """Response:""",
                "value": """Please share your thoughts on the discussion above""",
            }
        },
        "phase_instructions": "The user will respond to the second open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking a third open-ended question on the topic that builds on the previous discussion but explores new ideas. Provide context for the new question by building on the example you previous introduced for the topic.",
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
        "name": "Response",
        "fields": {
            "position": {
                "type": "text_area",
                "key": "topic2follow3",
                "height": 300,
                "label": """Response:""",
                "value": """Please respond considering the feedback above""",
            }
        },
        "phase_instructions": "The user will respond to the third open-ended question you presented to them. Respond to their response by gently challenge their thinking. Avoid long-term strategy and stay focused on immediate risks, trade-offs, and possible mitigation actions. Finish by asking them to summarize their short-term action plan in a concise, executive-ready response.",
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
                "label": """Mitigation plan:""",
                "value": """Please describe your mitigation plan""",
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
    "page_title": "SC3x 1T2025, Case Study, Short-term Impact Discussion V2",
    #"page_icon": "🗣️️",
    "layout": "centered",
    #"initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())

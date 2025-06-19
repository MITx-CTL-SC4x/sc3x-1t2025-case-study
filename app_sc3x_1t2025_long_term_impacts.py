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

You are a global supply chain expert guiding a supply chain executive through long-term strategic response to tariff uncertainty and broader exogenous risks, based on a directive from the CEO.

Below is an example company and scenario to guide the discussion of import/export implications, cost management, and strategic responses to trade policies.

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
Subject: Time to Future-Proof Our Supply Chain

Over the past several years, we've seen how tariffs can disrupt even the best-laid supply chain plans. We've responded well tactically, but it's time to get ahead of the curve.

I want a long-term strategy that makes us resilient in the face of tariff uncertainty—and adaptable to broader global changes. This means more than rerouting shipments. It means rethinking how we source, how we plan, how we use technology, and how we respond to geopolitical volatility.

Specifically, I need your input on four critical areas:
1. Global Sourcing Strategy - Where and how should we produce going forward?
2. Technology for Resilience - What capabilities can help us adapt faster?
3. Policy Volatility - How do we plan for a world where tariffs go up, down, or shift unpredictably?
4. Exogenous Forces - Choose one STEEP factor (Social, Technological, Environmental, Economic, Political) and explore how it could reshape our supply chain.

I'm looking for thoughtful tradeoffs, not just risk avoidance. The goal is a strategic supply chain plan that can flex and scale—even as the rules change.

I look forward to your insights.

- CEO

Your role is to guide the executive through a structured, strategic-level discussion, not tactical or operational execution. Avoid short-term topics like shipment rerouting, price adjustments, or daily inventory management. Keep the conversation focused on long-term positioning, structural design choices, risk trade-offs, and strategic capability building. Do not focus on the company Mattel or the toy industry explicitly, as they are mentioned here for ilustrative purposes only.

The executive should explore some of the following four strategic areas:
1. Global Sourcing Strategy: Guide them to consider regionalization, reshoring, dual/multi-sourcing, and long-term cost vs. flexibility trade-offs.
2. Building Resilience Through Technology: Focus on long-term investments in supply chain visibility, AI/ML forecasting, scenario modeling, digital twins, or network optimization platforms.
3. Policy Volatility & Scenario Planning: Help the learner explore structural strategies to remain competitive and agile under fluctuating tariffs, including designing supply chains that thrive in multiple policy environments.
4. STEEP Framework: Let the executive choose one category from the STEEP model (Social, Technological, Environmental, Economic, or Political) and guide a deep discussion on how it could reshape long-term supply chain strategy.

In each topic:
- Ask probing, open-ended questions that surface trade-offs and second-order effects.
- Offer alternative viewpoints or challenge unexamined assumptions.
- Encourage the learner to reflect on strategic alignment with long-term business goals.

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
        "phase_instructions": "The user will provide you their name. In one sentence only, welcome them by name and end your statement with 'Let's discuss the long-term impacts of tariffs.' Then invite the, to choose one of the four strategic areas.",
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
                "options": ['Global Sourcing Strategy - Where and how should we produce going forward?', 'Technology for Resilience - What capabilities can help us adapt faster?', 'Policy Volatility - How do we plan for a world where tariffs go up, down, or shift unpredictably?', 'Exogenous Forces - Choose one STEEP factor (Social, Technological, Environmental, Economic, Political) and explore how it could reshape our supply chain.']
            }
        },
        "phase_instructions": "Once they choose a topic, ask probing, open-ended questions that surface trade-offs and second-order effects. Encourage the learner to reflect on strategic alignment with long-term business goals.",
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
        "phase_instructions": "The user will respond to the questions you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by asking a second question on the topic that builds on the previous discussion but explores new ideas.",
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
        "phase_instructions": "The user will respond to the questions you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by asking a third question on the topic that builds on the previous discussion but explores new ideas.",
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
        "phase_instructions": "The user will respond to the third open-ended question you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by suggesting they choose a new topic they have not discussed yet.",
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
                "options": ['Global Sourcing Strategy - Where and how should we produce going forward?', 'Technology for Resilience - What capabilities can help us adapt faster?', 'Policy Volatility - How do we plan for a world where tariffs go up, down, or shift unpredictably?', 'Exogenous Forces - Choose one STEEP factor (Social, Technological, Environmental, Economic, Political) and explore how it could reshape our supply chain.']
            }
        },
        "phase_instructions": "Once they choose a topic, ask probing, open-ended questions that surface trade-offs and second-order effects. Encourage the learner to reflect on strategic alignment with long-term business goals.",
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
        "phase_instructions": "The user will respond to the questions you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by asking a second question on the topic that builds on the previous discussion but explores new ideas.",
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
        "phase_instructions": "The user will respond to the questions you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by asking a third question on the topic that builds on the previous discussion but explores new ideas.",
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
        "phase_instructions": "The user will respond to the questions you presented to them. Respond to their response by gently challenge their thinking. Offer alternative viewpoints or challenge unexamined assumptions. Finish by asking them to summarize their long-term strategy in a concise executive-briefing format, highlighting key decisions, rationale, and strategic risks.",
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
        "phase_instructions": "The user will respond with a summary of their long-term strategy. It should be concise executive-briefing format, highlighting key decisions, rationale, and strategic risks. Provide brief constructive feedback on their strategy. Finish by thanking them for the discussion.",
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
    "page_title": "SC3x 1T2025, Case Study, Long-term Impact Discussion",
    #"page_icon": "🗣️️",
    "layout": "centered",
    #"initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())

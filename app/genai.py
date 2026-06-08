def generate_ai_insight(prediction, remark):

    remark = remark.lower()

    if prediction=="Unsatisfied":

        if "delay" in remark:

            return """
Customer dissatisfaction appears related to delivery delay.

Recommended Actions:
• Improve delivery tracking
• Reduce shipping delays
• Prioritize urgent orders
"""

        elif "support" in remark:

            return """
Customer dissatisfaction appears related to customer support.

Recommended Actions:
• Improve support response time
• Prioritize complaint resolution
"""

        elif "quality" in remark:

            return """
Customer dissatisfaction appears related to product quality.

Recommended Actions:
• Strengthen product quality checks
• Improve product inspection
"""

        else:

            return """
Customer appears dissatisfied.

Recommended Actions:
• Further customer analysis required
"""

    else:

        return """
Customer experience appears positive.

Recommended Actions:
• Maintain service quality
• Continue customer engagement
"""
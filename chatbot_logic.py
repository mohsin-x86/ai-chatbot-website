def get_response(message):
    message = message.lower()

    # Greetings
    if any(word in message
           for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! Welcome to our support system. How can I help you today?"

    # Pricing & Payment
    elif any(
            word in message for word in
        ["price", "cost", "charges", "fee", "payment", "invoice", "bill"]):
        return "Our pricing depends on the service. Please contact sales@example.com for detailed pricing."

    # Services
    elif any(word in message for word in
             ["services", "solutions", "offer", "provide", "products"]):
        return "We provide IT support, software development, AI automation, and business solutions."

    # Contact Information
    elif any(word in message
             for word in ["contact", "email", "phone", "number", "address"]):
        return "You can contact us at support@example.com or call +971-000-0000."

    # Working Hours
    elif any(word in message
             for word in ["hours", "timing", "open", "close", "working time"]):
        return "Our working hours are Monday to Friday, 9 AM to 6 PM."

    # Technical Support
    elif any(word in message for word in
             ["error", "issue", "problem", "bug", "not working", "crash"]):
        return "Please describe your issue in detail so our technical team can assist you."

    # Account Related
    elif any(word in message for word in
             ["account", "login", "password", "reset", "signup", "register"]):
        return "For account-related issues, please use the password reset option or contact support."

    # Delivery
    elif any(word in message
             for word in ["delivery", "shipping", "order status", "tracking"]):
        return "You can track your order using the tracking number sent to your email."

    # Refund
    elif any(word in message
             for word in ["refund", "return", "cancel", "money back"]):
        return "Refund requests are processed within 5–7 business days."

    # AI Questions
    elif any(
            word in message for word in
        ["ai", "artificial intelligence", "machine learning", "automation"]):
        return "Our AI systems are designed to automate business workflows and enhance efficiency."

    # Security
    elif any(word in message
             for word in ["security", "privacy", "data protection", "safe"]):
        return "We prioritize data security and follow industry best practices."

    # Installation
    elif any(word in message
             for word in ["install", "setup", "configuration"]):
        return "Our team provides full installation and configuration support."

    # Maintenance
    elif any(word in message
             for word in ["maintenance", "update", "upgrade", "support plan"]):
        return "We offer regular maintenance and upgrade services for all clients."

    # Careers
    elif any(word in message
             for word in ["career", "job", "vacancy", "hiring", "apply"]):
        return "You can check our careers page for current job openings."

    # Location
    elif any(word in message
             for word in ["location", "office", "where are you", "branch"]):
        return "Our main office is located in Dubai, UAE."

    # Custom Development
    elif any(word in message
             for word in ["custom", "project", "development", "build system"]):
        return "We provide custom software development tailored to business needs."

    # Cloud Services
    elif any(word in message
             for word in ["cloud", "hosting", "server", "deployment"]):
        return "We offer cloud hosting and server deployment services."

    # Data Services
    elif any(word in message
             for word in ["data", "database", "analytics", "reporting"]):
        return "We provide data management and analytics solutions."

    # API
    elif any(word in message
             for word in ["api", "integration", "connect system"]):
        return "We support API integrations with third-party systems."

    # Greetings Variation
    elif "thank" in message:
        return "You're welcome! Let me know if you need further assistance."

    elif "bye" in message or "goodbye" in message:
        return "Thank you for visiting. Have a great day!"

    # 80+ Generic Business Conditions
    elif any(word in message for word in [
            "contract", "agreement", "proposal", "quote", "estimate", "demo",
            "trial", "subscription", "plan", "premium", "basic", "enterprise",
            "features", "benefits", "consultation", "meeting", "schedule",
            "appointment", "complaint", "feedback", "review", "rating",
            "upgrade", "downgrade", "technical team", "support team",
            "helpdesk", "system error", "network", "wifi", "software",
            "hardware", "printer", "scanner", "backup", "restore",
            "performance", "speed", "optimize", "analytics", "dashboard",
            "crm", "erp", "inventory", "billing", "management", "tracking",
            "monitoring", "compliance", "license", "renewal", "expiry",
            "training", "documentation", "guide", "manual", "tutorial",
            "implementation", "integration", "migration", "scalability",
            "reliability", "availability", "uptime", "sla", "compliance",
            "gdpr", "encryption", "firewall", "authentication",
            "authorization", "cloud storage", "virtual machine",
            "database server", "load balancing", "automation tool", "chatbot",
            "virtual assistant", "ai bot", "nlp", "deep learning",
            "neural network", "model", "prediction", "analysis",
            "classification", "recognition", "verification",
            "authentication system"
    ]):
        return "Thank you for your query. Our team will assist you with detailed information shortly."

    else:
        return "I'm sorry, I didn't fully understand your request. Could you please rephrase?"

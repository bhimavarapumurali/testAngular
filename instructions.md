# Re-creating the copilot-instructions.md file after execution state reset

updated_content = """# 🚀 GitHub Copilot Instructions for Email Rewriting  

## 📌 Purpose  
This guide helps **rewrite emails** to be more **professional, clear, and concise** using GitHub Copilot.  

---

## 📝 **How to Use Copilot for Email Rewriting**  

### 🔹 **Prompt Template**
```
Rewrite the following email to be more professional, polite, and concise:  

[Paste your email here]
```

### 🎯 **Customization Options**
- Make it **formal/casual** based on the context  
- Improve **clarity and sentence structure**  
- Ensure a **polite and professional** tone  
- Shorten **long sentences** for readability  

---

## ✅ **Example Prompts and Outputs**  

### 📌 **1. Meeting Request Email**  

**📝 Original Email:**  
> "Hey, can we have a meeting tomorrow about the new feature? Let me know what time works."  

**🛠️ Copilot Prompt:**  
```
Rewrite this email to be more professional and structured.
```

**🚀 Copilot Output:**  
```
Subject: Meeting Request for New Feature Discussion  

Hi [Recipient's Name],  

I hope you're doing well. I’d like to schedule a meeting to discuss the new feature. Please let me know your availability for tomorrow, and I’ll coordinate accordingly.  

Looking forward to your response.  

Best regards,  
[Your Name]  
```

---

### 📌 **2. Follow-up on Pending Task**  

**📝 Original Email:**  
> "Just checking if you got a chance to look at the report. Please update me."  

**🛠️ Copilot Prompt:**  
```
Rewrite this email to be more polite and professional.
```

**🚀 Copilot Output:**  
```
Subject: Follow-up on Report Review  

Hi [Recipient's Name],  

I hope you’re doing well. I wanted to follow up on the report I shared earlier. Please let me know if you had a chance to review it and share any feedback at your convenience.  

Looking forward to your update.  

Best regards,  
[Your Name]  
```

---

## 🎯 **Best Practices for Email Rewriting**  
✅ **Use Clear Subject Lines**  
✅ **Keep It Concise & To the Point**  
✅ **Maintain a Polite & Professional Tone**  
✅ **Provide Context Before the Request**  
✅ **Include a Call to Action (Next Steps)**  

---

## 🔧 **Automate Email Rewriting with Copilot**  

### 🔹 **Quick Prompt for Copilot**  
```
Rewrite this email to be more professional, polite, and concise:  
[Paste your email here]
```

### 🔹 **Advanced Prompt for Customization**  
```
Rewrite this email to be more [Formal/Casual], keeping it concise and polite.  
Make it sound [More Persuasive/Direct/Diplomatic].  
[Paste your email here]
```

---

# ✉️ Summarizing Email Chains with GitHub Copilot

GitHub Copilot can assist in condensing lengthy email threads into concise summaries, highlighting key points and decisions.

### 🔹 **Prompt Template**
```
Summarize the following email thread, highlighting key points, decisions made, and action items:  

[Paste the email thread here]
```

### 🎯 **Customization Options**
- **Focus Areas**: Specify if you want to emphasize decisions, action items, or general information.
- **Length**: Indicate if you prefer a brief summary or a detailed one.
- **Tone**: Choose between formal or informal language based on your audience.

### ✅ **Example**

**📝 Input Email Thread:**
> *Email 1:*  
> **Subject: Project Update**  
>  
> Hi Team,  
> We've completed the initial phase of the project. Let's discuss the next steps.  
>  
> Best,  
> Alice  
>  
> *Email 2:*  
> **Subject: Re: Project Update**  
>  
> Hi Alice,  
> Great work! I suggest we meet tomorrow to plan the next phase.  
>  
> Regards,  
> Bob  
>  
> *Email 3:*  
> **Subject: Re: Project Update**  
>  
> Hi All,  
> Tomorrow works for me. What time?  
>  
> Thanks,  
> Carol  

**🚀 Copilot Output:**
```
Summary of Email Thread:

- **Project Update**: Initial phase completed.
- **Next Steps**: Team meeting proposed to plan the next phase.
- **Action Items**:
  - Schedule a meeting for tomorrow; time to be determined.
```

### 🎯 **Best Practices**
- **Clarity**: Ensure the summary captures the essence of the conversation without unnecessary details.
- **Accuracy**: Reflect all key decisions and action items accurately.
- **Brevity**: Keep the summary concise to facilitate quick understanding.

---

This file ensures **Copilot understands email rewriting and summarization**, providing users with clear and structured email outputs.
"""

# Save the updated content to a markdown file
file_path = "/mnt/data/copilot-instructions.md"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(updated_content)

# Provide the download link
file_path
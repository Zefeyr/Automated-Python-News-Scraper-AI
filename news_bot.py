import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from newspaper import Article
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv()

# --- AI SETUP (Direct Model Usage) ---
print("🤖 Loading AI Model weights into memory...")
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def ai_summarize(text):
    """Bypasses the broken pipeline helper to summarize directly"""
    try:
        # Prepare the text for the model
        inputs = tokenizer([text[:2000]], max_length=1024, return_tensors="pt", truncation=True)
        
        # Generate summary IDs
        summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=80)
        
        # Decode back to English
        return tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    except:
        return "Could not generate AI synopsis."

def get_tech_news():
    print("🛰️  Scraping and Summarizing...")
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('span', class_='titleline')
    
    report = "🚀 YOUR DAILY AI-SUMMARIZED BRIEFING\n"
    report += "--------------------------------------\n\n"
    
    for i, article in enumerate(articles[:3], 1):
        title = article.text
        link = article.find('a')['href']
        
        try:
            # Extract content
            news_article = Article(link)
            news_article.download()
            news_article.parse()
            
            # Use our new manual AI function
            synopsis = ai_summarize(news_article.text)
            
        except Exception:
            synopsis = "AI could not process this source."
            
        report += f"{i}. {title.upper()}\n"
        report += f"   🤖 AI SYNOPSIS: {synopsis}\n"
        report += f"   🔗 {link}\n\n"
        print(f"✅ Processed {i}/3")
    
    return report

def send_email(content):
    EMAIL_ADDR = os.getenv("EMAIL_USER")
    APP_PASSWORD = os.getenv("EMAIL_PASS")
    
    print("📧 Sending email...")
    msg = EmailMessage()
    msg['Subject'] = 'Tech News Automation Success! 🤖'
    msg['From'] = EMAIL_ADDR
    msg['To'] = EMAIL_ADDR
    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDR, APP_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    try:
        news_data = get_tech_news()
        send_email(news_data)
        print("✅ DONE! Check your inbox, my bro.")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")
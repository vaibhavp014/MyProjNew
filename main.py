import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

# In-memory blog post storage
blog_posts = [
    {
        'id': 1,
        'title': 'The Future of Digital Marketing',
        'content': '''
        <p>Digital marketing continues to evolve at a rapid pace. With the advent of AI and machine learning, personalization has reached new heights. Brands can now deliver highly targeted content that resonates with individual users based on their preferences, behavior, and history.</p>
        
        <p>Voice search optimization is becoming increasingly important as more consumers use voice assistants like Alexa, Siri, and Google Assistant. This shift requires marketers to adapt their SEO strategies to account for more conversational, long-tail keywords and natural language queries.</p>
        
        <p>Video content remains king, with short-form videos dominating platforms like TikTok, Instagram Reels, and YouTube Shorts. Brands that can tell compelling stories in bite-sized formats are seeing significant engagement and conversion rates.</p>
        
        <p>As we move forward, ethical marketing and transparency will be crucial. Consumers are becoming more discerning and value brands that are authentic, sustainable, and socially responsible.</p>
        ''',
        'author': 'Marketing Team',
        'date': datetime(2023, 11, 15),
        'image': 'https://source.unsplash.com/random/800x600/?marketing',
        'summary': 'Exploring the latest trends in digital marketing and what the future holds for brands online.'
    },
    {
        'id': 2,
        'title': 'Building a Strong Brand Identity',
        'content': '''
        <p>A strong brand identity is the foundation of any successful business. It's more than just a logo or a catchy slogan—it encompasses the entire perception of your company in the minds of your customers and the general public.</p>
        
        <p>Consistency is key when it comes to brand identity. From your visual elements to your messaging, maintaining a uniform presence across all platforms helps reinforce your brand in the minds of consumers. This includes your website, social media profiles, packaging, and any other customer touchpoints.</p>
        
        <p>Understanding your target audience is crucial for developing a brand identity that resonates. Conduct thorough market research to identify your ideal customers' preferences, pain points, and values. This information will inform your brand positioning and messaging strategy.</p>
        
        <p>Your brand's personality should shine through in all communications. Whether your brand is friendly, professional, innovative, or luxurious, consistency in tone and voice helps build a connection with your audience.</p>
        
        <p>Remember, a strong brand identity is an investment that pays dividends over time through increased customer loyalty, recognition, and trust.</p>
        ''',
        'author': 'Brand Strategist',
        'date': datetime(2023, 10, 20),
        'image': 'https://source.unsplash.com/random/800x600/?branding',
        'summary': 'Learn the essential elements of creating a strong, memorable brand identity that connects with your audience.'
    },
    {
        'id': 3,
        'title': 'Content Marketing Strategies That Convert',
        'content': '''
        <p>Content marketing continues to be a powerful tool for attracting and engaging potential customers. When done right, it not only drives traffic but also converts visitors into loyal customers.</p>
        
        <p>Start with a solid content strategy aligned with your business goals. Whether you're looking to increase brand awareness, generate leads, or drive sales, your content should be purposefully designed to move users through the sales funnel.</p>
        
        <p>Quality always trumps quantity. Creating valuable, informative, and engaging content that addresses your audience's needs and pain points will establish your brand as an authority in your industry. This trust is a crucial factor in conversion.</p>
        
        <p>Diversify your content formats to cater to different preferences. Blog posts, videos, podcasts, infographics, and interactive tools can all play important roles in your content ecosystem. Each format has its strengths and can reach audiences at different stages of the buyer's journey.</p>
        
        <p>Don't forget to optimize your content for search engines. SEO-friendly content ensures that your target audience can find you when they're actively searching for solutions you provide. This intent-driven discovery often leads to higher conversion rates.</p>
        
        <p>Finally, always include clear calls to action. Guide your audience on what to do next, whether it's subscribing to a newsletter, downloading a resource, or making a purchase.</p>
        ''',
        'author': 'Content Strategist',
        'date': datetime(2023, 9, 5),
        'image': 'https://source.unsplash.com/random/800x600/?content',
        'summary': 'Discover effective content marketing strategies that not only engage your audience but drive meaningful conversions.'
    },
    {
        'id': 4,
        'title': 'Social Media Trends for 2024',
        'content': '''
        <p>Social media continues to evolve rapidly, with new platforms, features, and trends emerging constantly. Staying ahead of these changes is essential for brands looking to maintain and grow their online presence.</p>
        
        <p>One of the biggest trends we're seeing is the rise of social commerce. Platforms are increasingly integrating shopping features, allowing users to discover and purchase products without leaving the app. This seamless experience is changing the e-commerce landscape.</p>
        
        <p>Authenticity is becoming more important than ever. Users are gravitating toward genuine, unfiltered content over highly produced, polished posts. Brands that showcase their human side and create relatable content are building stronger connections with their audiences.</p>
        
        <p>Ephemeral content—temporary posts that disappear after 24 hours—continues to gain popularity. Stories on Instagram, Facebook, and now LinkedIn are becoming key components of social media strategies, offering a way to share timely, in-the-moment content.</p>
        
        <p>Niche communities are thriving as users seek more meaningful interactions. Brands that can identify and engage with these communities authentically have an opportunity to build loyal followings.</p>
        
        <p>As we look toward 2024, expect to see more augmented reality features, increased use of AI for personalization, and a continued focus on video content across all platforms.</p>
        ''',
        'author': 'Social Media Expert',
        'date': datetime(2023, 12, 1),
        'image': 'https://source.unsplash.com/random/800x600/?social',
        'summary': 'Explore the emerging social media trends that will shape brand strategies in 2024 and beyond.'
    }
]

@app.route('/')
def index():
    # Get the 2 most recent blog posts for the homepage
    recent_posts = sorted(blog_posts, key=lambda x: x['date'], reverse=True)[:2]
    return render_template('index.html', recent_posts=recent_posts)

@app.route('/blog')
def blog():
    # Sort blog posts by date (newest first)
    sorted_posts = sorted(blog_posts, key=lambda x: x['date'], reverse=True)
    return render_template('blog.html', posts=sorted_posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    # Find the post with the given ID
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('blog_post.html', post=post)
    else:
        abort(404)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

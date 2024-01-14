from supabase import create_client, Client

url = "https://icvzwfgjdjyzvogalfsr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imljdnp3ZmdqZGp5enZvZ2FsZnNyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDUxNjY3MTksImV4cCI6MjAyMDc0MjcxOX0.RaiHts72Fap8jRjr5Lra0RsCsc9WtIm7KBaYAXMMbGY"
supabase: Client = create_client(url, key)

response = supabase.table("recipes").select("*").execute()

# Grab a specific food object based off name:
food = supabase.table("recipes").select('*').eq('name', 'Swedish Baked Beans').execute() #.eq('name', 'user_input')

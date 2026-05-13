import { useState } from 'react'
function App() {
const [question, setQuestion] = useState('')
const [messages, setMessages] = useState([])
const [loading, setLoading] = useState(false)
const askQuestion = async () => {
if (!question.trim()) return
const userMessage = {
role: 'user',
content: question,
}
setMessages((prev) => [...prev, userMessage])
const currentQuestion = question
setQuestion('')
setLoading(true)
try {
const response = await fetch(
'http://127.0.0.1:8000/ask',
{
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
body: JSON.stringify({
question: currentQuestion,
}),
}
)
const data = await response.json()
const botMessage = {
role: 'assistant',
content: data.answer,
}
setMessages((prev) => [...prev, botMessage])
} catch (error) {
console.error(error)
}
setLoading(false)
}
return (
<div className="flex h-screen bg-slate-950 text-white">
{/* Sidebar */}
<div className="w-64 bg-slate-900 border-r border-slate-800 p-4 hidden
md:block">
<h1 className="text-2xl font-bold mb-8">
RAG AI
</h1>
<button
className="w-full bg-slate-800 hover:bg-slate-700 transition p-3 rounded-xl
text-left">
+ New Chat
</button>
<div className="mt-8 text-sm text-slate-400">
Local RAG System
</div>
</div>
{/* Main Chat Area */}
<div className="flex flex-col flex-1">
{/* Header */}
<div className="border-b border-slate-800 p-4 text-xl font-semibold bgslate-900">
AI Assistant
</div>
{/* Messages */}
<div className="flex-1 overflow-y-auto px-4 py-6 space-y-6">
{
messages.length === 0 && (
  <div className="h-full flex items-center justify-center textslate-500 text-lg">
Ask anything about your documents
</div>
)
}
{
messages.map((message, index) => (
<div
key={index}
className={`flex ${
message.role === 'user'
? 'justify-end'
: 'justify-start'
}`}
>
<div
className={`max-w-2xl px-5 py-4 rounded-2xl shadow-lg
whitespace-pre-wrap ${
message.role === 'user'
? 'bg-blue-600 text-white'
: 'bg-slate-800 text-slate-100'
}`}
>
{message.content}
</div>
</div>
))
}
{
loading && (
<div className="flex justify-start">
<div
className="bg-slate-800 px-5 py-4 rounded-2xl animate-pulse text-slate-400">
Thinking...
</div>
</div>
)
}
</div>
{/* Input Area */}
<div className="border-t border-slate-800 bg-slate-900 p-4">
<div className="flex items-center gap-3 max-w-4xl mx-auto">
<textarea
rows="2"
placeholder="Ask a question..."
value={question}
onChange={(e) => setQuestion(e.target.value)}
className="flex-1 resize-none bg-slate-800 text-white rounded-2xl
px-4 py-3 outline-none border border-slate-700 focus:border-blue-500"
/>
<button
onClick={askQuestion}
className="bg-blue-600 hover:bg-blue-500 transition px-6 py-3
rounded-2xl font-semibold"
>
Send
</button>
</div>
</div>
</div>
</div>
)
}
export default App
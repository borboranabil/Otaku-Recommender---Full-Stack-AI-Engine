import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, Sparkles, BookOpen, Tv, Zap, Youtube } from "lucide-react"; // <--- Added Youtube Icon

export default function App() {
  const [query, setQuery] = useState("");
  const [mediaType, setMediaType] = useState("anime");
  const [smartSearch, setSmartSearch] = useState(false);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchRecommendations = async (overrideQuery = null) => {
    const searchTerm = overrideQuery || query;
    if (!searchTerm) return;

    if (overrideQuery) setQuery(overrideQuery);

    setLoading(true);
    setResults(null);

    try {
      // NOTE: If you deployed to Render, replace this URL with your Render URL
      // e.g., const url = `https://otaku-backend.onrender.com/recommend?...`;
      const url = `http://127.0.0.1:8000/recommend?media_type=${mediaType}&query=${searchTerm}&use_smart_search=${smartSearch}&topn=5`;
      
      const res = await fetch(url);
      if (!res.ok) throw new Error("Backend error");
      const data = await res.json();
      setResults(data);
    } catch (err) {
      console.error(err);
      alert("Failed to connect to backend. Is 'uvicorn api:app --reload' running?");
    }
    setLoading(false);
  };

  // Helper to open YouTube
  const openTrailer = (e, title) => {
    e.stopPropagation(); // <--- STOP the click from bubbling up to the card search
    window.open(`https://www.youtube.com/results?search_query=${title} ${mediaType} trailer`, "_blank");
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white font-sans p-8 flex flex-col items-center">
      <div className="w-full max-w-3xl space-y-8">
        <header className="text-center space-y-2">
          <h1 className="text-5xl font-extrabold bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent py-2">
            Otaku Recommender
          </h1>
          <p className="text-gray-400 text-lg">AI-Powered suggestions for your next obsession</p>
        </header>

        <div className="bg-gray-800 p-8 rounded-3xl shadow-2xl border border-gray-700 space-y-6">
          <div className="flex justify-center gap-4">
            {['anime', 'manga', 'manhwa'].map((type) => (
              <button
                key={type}
                onClick={() => setMediaType(type)}
                className={`px-6 py-2 rounded-full capitalize flex items-center gap-2 transition-all font-medium ${
                  mediaType === type 
                    ? "bg-violet-600 text-white shadow-lg shadow-violet-500/30 scale-105" 
                    : "bg-gray-700 text-gray-400 hover:bg-gray-600"
                }`}
              >
                {type === 'anime' ? <Tv size={18}/> : <BookOpen size={18}/>}
                {type}
              </button>
            ))}
          </div>

          <div className="relative group">
            <input
              type="text"
              placeholder={`Enter ${mediaType} title (e.g. "Naruto")...`}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && fetchRecommendations()}
              className="w-full bg-gray-900 border border-gray-700 rounded-2xl py-4 pl-14 pr-32 text-lg focus:ring-2 focus:ring-violet-500 focus:border-transparent outline-none transition-all group-hover:border-gray-600"
            />
            <Search className="absolute left-5 top-1/2 -translate-y-1/2 text-gray-500" size={24} />
            <button 
              onClick={() => fetchRecommendations()}
              className="absolute right-2 top-2 bottom-2 bg-violet-600 hover:bg-violet-500 text-white px-6 rounded-xl font-bold transition-all hover:scale-105 active:scale-95"
            >
              Go
            </button>
          </div>

          <div 
            onClick={() => setSmartSearch(!smartSearch)}
            className="flex items-center justify-between bg-gray-900/50 p-4 rounded-xl border border-gray-700 cursor-pointer hover:bg-gray-900 transition-colors"
          >
            <div className="flex items-center gap-3">
              <div className={`p-2 rounded-lg ${smartSearch ? "bg-yellow-500/20 text-yellow-400" : "bg-blue-500/20 text-blue-400"}`}>
                {smartSearch ? <Sparkles size={20}/> : <Zap size={20}/>}
              </div>
              <div className="flex flex-col">
                <span className="font-semibold text-gray-200">
                  {smartSearch ? "Semantic Search (AI)" : "Keyword Search (Fast)"}
                </span>
                <span className="text-xs text-gray-500">
                  {smartSearch ? "Understands meaning & context (Slower)" : "Matches exact words & titles (Instant)"}
                </span>
              </div>
            </div>
            
            <div className={`w-14 h-7 rounded-full p-1 transition-colors duration-300 ${smartSearch ? "bg-green-500" : "bg-gray-600"}`}>
              <div className={`w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-300 ${smartSearch ? "translate-x-7" : ""}`} />
            </div>
          </div>
        </div>

        <div className="space-y-4">
          {loading && (
            <div className="flex justify-center py-10">
              <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-violet-500"></div>
            </div>
          )}
          
          {results && (
            <AnimatePresence mode="wait">
              <motion.div 
                initial={{ opacity: 0, y: 20 }} 
                animate={{ opacity: 1, y: 0 }}
                className="space-y-4"
              >
                <div className="flex items-baseline justify-between px-2">
                  <h2 className="text-xl font-medium text-gray-300">
                    Results for <span className="text-violet-400 font-bold">"{results.base_title}"</span>
                  </h2>
                  <span className="text-xs text-gray-600 uppercase tracking-wider font-semibold">
                    via {results.engine_used}
                  </span>
                </div>
                
                <div className="grid gap-4">
                  {results.recommendations.map((rec, i) => (
                    <motion.div
                      key={rec.item_id}
                      layoutId={rec.item_id} 
                      onClick={() => fetchRecommendations(rec.title)}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: i * 0.1 }}
                      className="bg-gray-800 rounded-xl border border-gray-700 hover:border-violet-500 overflow-hidden flex group transition-all cursor-pointer hover:bg-gray-750 relative"
                    >
                      <div className="w-28 h-40 flex-shrink-0 overflow-hidden relative">
                        <img 
                          src={rec.image_url} 
                          alt={rec.title}
                          className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                        />
                      </div>

                      <div className="p-4 flex-grow flex flex-col justify-between">
                        <div className="flex justify-between items-start">
                          <div>
                            <h3 className="text-lg font-bold text-white group-hover:text-violet-400 transition-colors line-clamp-1">
                              {rec.title}
                            </h3>
                            <div className="flex flex-wrap gap-2 mt-2">
                              {rec.genres.split('|').slice(0, 3).map((g, idx) => (
                                <span key={idx} className="text-xs bg-gray-700 text-gray-300 px-2 py-1 rounded-md border border-gray-600">
                                  {g.trim()}
                                </span>
                              ))}
                            </div>
                          </div>
                          <div className="text-right pl-2">
                            <div className="text-2xl font-black text-gray-700 group-hover:text-violet-500 transition-colors">
                              {(rec.similarity_score * 100).toFixed(0)}%
                            </div>
                            <div className="text-[10px] text-gray-500 uppercase font-bold tracking-wider">Match</div>
                          </div>
                        </div>

                        {/* TRAILER BUTTON */}
                        <div className="mt-4 flex justify-end">
                            <button
                                onClick={(e) => openTrailer(e, rec.title)}
                                className="flex items-center gap-2 px-3 py-1.5 bg-red-600 hover:bg-red-500 text-white text-xs font-bold rounded-lg transition-colors shadow-lg"
                            >
                                <Youtube size={14} /> Watch Trailer
                            </button>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            </AnimatePresence>
          )}
        </div>
      </div>
    </div>
  );
}
export default function Header() {
  return (
    <header className="h-20 bg-white border-b border-gray-200 flex items-center justify-between px-8 shadow-sm">

      <div className="flex items-center gap-4">

        <div className="w-12 h-12 rounded-full bg-blue-600 flex items-center justify-center text-white text-xl font-bold">
          AI
        </div>

        <div>
          <h1 className="text-2xl font-bold text-gray-800">
            Namaste India Trip
          </h1>

          <p className="text-gray-500 text-sm">
            AI Travel Assistant
          </p>
        </div>

      </div>

      <button className="px-5 py-2 rounded-xl bg-blue-600 text-white hover:bg-blue-700 transition">
        New Chat
      </button>

    </header>
  );
}
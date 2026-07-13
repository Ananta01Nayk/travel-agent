import { Heart, X } from "lucide-react";
import logo from "../assets/logo.png";

export default function Header() {
  return (
    <header className="w-full flex justify-center px-8 pt-8 pb-6">

      <div
        className="
          w-full
          max-w-[1500px]
          rounded-[28px]
          border
          border-white/20
          bg-white/15
          backdrop-blur-2xl
          shadow-2xl
          px-8
          py-5
          flex
          items-center
          justify-between
        "
      >
        {/* Left */}

        <div className="flex items-center gap-5">

          <img
            src={logo}
            alt="logo"
            className="
              w-16
              h-16
              rounded-2xl
              object-cover
              shadow-lg
              bg-white
              p-1
            "
          />

          <div>

            <h1 className="text-3xl font-bold text-white">
              Namaste India Trip Agent
            </h1>

            <div className="flex items-center gap-2 mt-1">

              <span className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />

              <span className="text-white/90 text-sm">
                Online
              </span>

            </div>

          </div>

        </div>

        {/* Right */}

        <div className="flex items-center gap-3">

          <button
            className="
              w-12
              h-12
              rounded-xl
              bg-white/10
              backdrop-blur-xl
              hover:bg-white/20
              transition
              flex
              items-center
              justify-center
            "
          >
            <Heart
              size={22}
              className="text-white"
            />
          </button>

          <button
            className="
              w-12
              h-12
              rounded-xl
              bg-white/10
              backdrop-blur-xl
              hover:bg-red-500
              transition
              flex
              items-center
              justify-center
            "
          >
            <X
              size={22}
              className="text-white"
            />
          </button>

        </div>

      </div>

    </header>
  );
}
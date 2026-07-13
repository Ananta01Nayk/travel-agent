import { useEffect, useState } from "react";
import {
  ChevronLeft,
  ChevronRight,
  CalendarDays,
  IndianRupee,
  ExternalLink,
} from "lucide-react";

export default function RetrievalSidebar({ sources }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    setCurrentIndex(0);
  }, [sources]);

  if (!sources || sources.length === 0) return null;

  const item = sources[currentIndex];
  const totalPackages = sources.length;

  return (
    <div
      className="
        h-full
        rounded-[28px]
        bg-white/10
        backdrop-blur-xl
        border border-white/20
        shadow-[0_20px_60px_rgba(0,0,0,.25)]
        overflow-hidden
        flex
        flex-col
      "
    >
      {/* Header */}

      <div className="px-5 py-3 bg-white/5 border-b border-white/10">

        <div className="flex items-center justify-between">

          <div>

            <h2 className="text-base font-semibold text-white">
              AI Recommendations
            </h2>

            <p className="text-[11px] text-white/60 mt-0.5">
              Best matching travel package
            </p>

          </div>

          <span className="text-white text-sm font-medium">
            {currentIndex + 1} / {totalPackages}
          </span>

        </div>

      </div>

      {/* Image */}

      <div className="relative">

        <img
          src={item.image}
          alt={item.title}
          className="w-full h-36 object-cover"
        />

        <div className="absolute top-3 right-3">

          <span
            className="
              bg-green-600
              text-white
              text-xs
              px-3
              py-1
              rounded-full
              font-medium
              shadow
            "
          >
            ⭐ AI Pick
          </span>

        </div>

      </div>

      {/* Content */}

      <div className="flex-1 overflow-y-auto bg-white px-5 py-4">

        <h2 className="text-lg font-bold text-slate-900 leading-6">
          {item.title}
        </h2>

        <div className="mt-5 space-y-3">

          <div className="flex items-center gap-3">

            <IndianRupee
              size={18}
              className="text-blue-600"
            />

            <span className="font-bold text-slate-900">
              {item.price}
            </span>

          </div>

          <div className="flex items-center gap-3">

            <CalendarDays
              size={18}
              className="text-blue-600"
            />

            <span className="text-slate-600">
              {item.duration}
            </span>

          </div>

        </div>

        {/* Why */}

        <div className="mt-5 rounded-xl bg-slate-100 p-4">

          <h3 className="font-semibold text-slate-800">
            Why this package?
          </h3>

          <p className="text-sm text-slate-600 leading-6 mt-2">
            This recommendation closely matches your destination,
            duration and travel preferences based on our travel database.
          </p>

        </div>

        {/* Button */}

        <a
          href={item.detail_url}
          target="_blank"
          rel="noreferrer"
          className="mt-3"
        >

          <button
            className="
              mt-20
              w-full
              h-9
              rounded-lg
              bg-blue-600
              hover:bg-blue-700
              transition
              text-white
              text-[13px]
              font-semibold
              flex
              items-center
              justify-center
              gap-2
              shadow
            "
          >
            View Package

            <ExternalLink size={16} />

          </button>

        </a>

      </div>

      {/* Footer */}

      <div className="bg-white border-t px-5 py-2">

        <div className="flex items-center justify-between">

          <button
            onClick={() =>
              setCurrentIndex(
                currentIndex === 0
                  ? totalPackages - 1
                  : currentIndex - 1
              )
            }
            className="
              w-8
              h-8
              rounded-full
              border
              border-slate-300
              hover:border-blue-500
              hover:bg-blue-50
              transition
              flex
              items-center
              justify-center
            "
          >
            <ChevronLeft size={14} />
          </button>

          <span className="text-[11px] font-semibold text-slate-500 tracking-wide">
            {currentIndex + 1} of {totalPackages}
          </span>

          <button
            onClick={() =>
              setCurrentIndex(
                currentIndex === totalPackages - 1
                  ? 0
                  : currentIndex + 1
              )
            }
            className="
              w-9
              h-8
              rounded-full
              border
              border-slate-300
              hover:border-blue-500
              hover:bg-blue-50
              transition
              flex
              items-center
              justify-center
            "
          >
            <ChevronRight size={16} />
          </button>

        </div>

      </div>

    </div>
  );
}
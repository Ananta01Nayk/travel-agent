export default function RetrievalSidebar({ sources }) {

  return (

    <div className="bg-white rounded-[30px] shadow-xl h-full flex flex-col overflow-hidden">

      <div className="p-6 border-b">

        <h2 className="text-2xl font-bold">
          Retrieved Packages
        </h2>

      </div>

      <div className="flex-1 overflow-y-auto p-6">

        {sources.length === 0 ? (

          <p className="text-gray-400">

            Ask a question to retrieve packages.

          </p>

        ) : (

          <div className="space-y-4">

            {sources.map((item, index) => (

              <div

                key={index}

                className="rounded-2xl border overflow-hidden shadow hover:shadow-lg transition"

              >

                <img

                  src={item.image}

                  alt={item.title}

                  className="w-full h-40 object-cover"

                />

                <div className="p-4">

                  <h3 className="font-bold">

                    {item.title}

                  </h3>

                  <p className="text-blue-600 font-semibold">

                    {item.price}

                  </p>

                  <p className="text-gray-500">

                    {item.duration}

                  </p>

                  <a

                    href={item.detail_url}

                    target="_blank"

                    rel="noreferrer"

                    className="text-blue-600 text-sm"

                  >

                    View Details →

                  </a>

                </div>

              </div>

            ))}

          </div>

        )}

      </div>

    </div>

  );

}
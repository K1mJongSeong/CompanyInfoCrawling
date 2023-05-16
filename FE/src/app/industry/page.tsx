import Img from "@/components/common/Image";
import Link from "next/link";

export default function IndustryPage() {
  return (
    <div
      className="w-screen relative flex items-center justify-center py-10 bg-fixed min-h-[900px]"
      style={{
        backgroundImage: "url('/assets/images/industry_bg.png",
        backgroundPosition: "center",
      }}
    >
      <div className="relative flex flex-col w-[calc(100%-32px)] max-w-2xl gap-7 xl:max-w-4xl">
        <div className="flex flex-col overflow-hidden bg-white rounded-lg xl:flex-row">
          <div className="w-full xl:w-1/2">
            <Img src={"/assets/images/industry_1.png"} alt="client" />
          </div>
          <div className="flex flex-col items-end justify-center w-full px-2 py-4 xl:w-1/2 xl:py-10 xl:px-11">
            <div className="flex flex-col w-full">
              <h3 className="mb-3 text-lg font-bold">Clients</h3>
              <p className="mb-10 text-xs text-gray-700">
                We have global clients from the diverse industry
                <br />
                including investment company, law firm, manufacturing <br />
                company, IT-based start-up, government-affiliated organisation.
                <br />​ <br />
                ​Sentinel Korea offers tailored consulting services which
                <br />
                minimise security and business risks.
              </p>
            </div>
            <Link
              className="flex gap-1 text-sm text-blue-400 whitespace-nowrap"
              href={"/"}
            >
              GO TO SEARCH
              <Img
                src={"/assets/images/arrow.svg"}
                alt="arrow"
                className="w-7"
              />
            </Link>
          </div>
        </div>
        <div className="flex flex-col overflow-hidden bg-white rounded-lg xl:flex-row">
          <div className="flex flex-col items-end justify-center order-2 w-full px-2 py-4 xl:w-1/2 xl:py-16 xl:px-11 xl:order-1">
            <div className="flex flex-col w-full">
              <h3 className="mb-3 text-lg font-bold">Partners</h3>
              <p className="mb-10 text-xs text-gray-700">
                We have developed a global network in various business sectors.
                <br />
                Our partners are highly professional and have the top
                <br />
                technologies and experiences in their fields.
                <br /> We are very proud of working with our partners.
                <br />
                <br />​ Having built a strong partnership internationally, we
                respect the <br />
                diversity in the global business. Thus, Sentinel Korea always
                <br />
                welcomes domestic and international partnerships.
              </p>
            </div>
            <Link
              className="flex gap-1 text-sm text-blue-400 whitespace-nowrap"
              href={"https://www.sentinelkorea.com/"}
            >
              CONTACT US
              <Img
                src={"/assets/images/arrow.svg"}
                alt="arrow"
                className="w-7"
              />
            </Link>
          </div>
          <div className="order-1 w-full h-full xl:w-1/2 xl:order-2">
            <Img src={"/assets/images/industry_2.png"} alt="client" />
          </div>
        </div>
      </div>
    </div>
  );
}

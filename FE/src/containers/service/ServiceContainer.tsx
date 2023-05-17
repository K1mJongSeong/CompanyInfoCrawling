"use client";
import CustomizedAccordions from "@/components/service/Accordion";
import { InFaqProps } from "@/service/service_service";
import Link from "next/link";
import { SyntheticEvent, useState } from "react";

export default function ServiceContainer({
  qnaList,
}: {
  qnaList: Array<InFaqProps>;
}) {
  const [expanded, setExpanded] = useState<string | false>("panel0");
  const handleChangeAct =
    (panel: string) => (event: React.SyntheticEvent, newExpanded: boolean) => {
      setExpanded(newExpanded ? panel : false);
    };
  return (
    <div
      className="w-screen relative flex flex-col items-center justify-center gap-6 py-10 bg-fixed  min-h-[900px]"
      style={{
        backgroundImage: "url('/assets/images/service_bg.png",
        backgroundPosition: "center",
      }}
    >
      <div className="w-[calc(100%-32px)] max-w-7xl bg-white rounded-lg py-8 px-5 pb-11 flex flex-col items-center">
        <h2 className="mb-1 text-lg font-bold uppercase">SERVICE</h2>
        <p className="text-sm text-gray-700 mb-[40px]">
          Experience the services offered by Sentinel Korea!
        </p>
        <div className="flex flex-col justify-between w-full lg:flex-row">
          <div className="flex flex-col gap-5 px-0 py-4 border-b border-gray-200 lg:border-b-0 lg:border-r lg:px-10 lg:py-7">
            <div className="flex flex-col gap-2">
              <div className="font-bold text-blue-500">DD1, DD2</div>
              <p className="text-sm">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                <br />
                industry. Lorem Ipsum has been the {`industry's`} standard dummy
                <br />
                text ever since the 1500s, when an unknown printer took a galley
                <br />
                of type and scrambled it to make a type specimen book.
              </p>
            </div>
            <div className="flex flex-col gap-2">
              <div className="font-bold text-blue-500">DD3</div>
              <p className="text-sm">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                <br />
                industry. Lorem Ipsum has been the {`industry's`} standard dummy
                <br />
                text ever since the 1500s, when an unknown printer took a galley
                <br />
                of type and scrambled it to make a type specimen book.
              </p>
            </div>
          </div>
          <div className="flex flex-col flex-1 px-0 py-4 lg:px-10 lg:py-7">
            <div className="mb-2 font-bold text-blue-500">Annual Payment</div>
            <p className="mb-8 text-sm">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the {`industry's`} standard dummy
              text ever since the 1500s, when an unknown printer took a galley
              of type and scrambled it to make a type specimen book.
            </p>
            <div className="flex justify-end">
              <button className="w-full max-w-[200px] h-[40px] bg-indigo-900 text-white rounded-md hover:bg-indigo-800">
                $0000
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="w-[calc(100%-32px)] max-w-7xl bg-white rounded-lg py-8 px-5 pb-11 flex flex-col items-center">
        <h2 className="mb-1 text-lg font-bold uppercase">FAQs</h2>
        <p className="text-sm text-gray-700 mb-[40px]">
          frequently asked questions
        </p>
        <div className="flex flex-col justify-between w-full mb-5">
          <CustomizedAccordions
            data={qnaList}
            expanded={expanded}
            handleChange={handleChangeAct}
          />
        </div>
        <div className="flex justify-end w-full md:px-10">
          <Link
            href={"/service/faqs"}
            className="w-full flex justify-center items-center max-w-[200px] h-[40px] bg-indigo-900 text-white rounded-md hover:bg-indigo-800"
          >
            VIEW ALL
          </Link>
        </div>
      </div>
    </div>
  );
}

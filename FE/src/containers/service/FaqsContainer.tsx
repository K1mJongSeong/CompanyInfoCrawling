"use client";

import PaginationBox from "@/components/common/Pagination";
import CustomizedAccordions from "@/components/service/Accordion";
import { InFaqProps, getQnaList } from "@/service/service_service";
import { useState } from "react";
import { useQuery } from "react-query";

export default function FaqsContainer() {
  const [page, setPage] = useState<number>(1);
  const [totalPage, setTotalPage] = useState<number>(1);
  const [list, setList] = useState<Array<InFaqProps>>([]);
  const [expanded, setExpanded] = useState<string | false>("panel0");

  const faqsListQueryKey = ["faqsList", page];
  useQuery(
    faqsListQueryKey,
    async () => await getQnaList({ page: String(page) }),
    {
      keepPreviousData: true,
      refetchOnWindowFocus: false,
      onSuccess: (data: Array<InFaqProps>) => {
        console.log("data", data);
        setList(data);
        setTotalPage(parseInt(data[0].total_page_num, 10));
        setExpanded("panel0");
      },
    }
  );
  const handleChangeAct =
    (panel: string) => (event: React.SyntheticEvent, newExpanded: boolean) => {
      setExpanded(newExpanded ? panel : false);
    };

  const handleChangePage = (
    event: React.ChangeEvent<unknown>,
    value: number
  ) => {
    setPage(value);
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
        <h2 className="mb-1 text-lg font-bold uppercase">ALL FAQs</h2>
        <p className="text-sm text-gray-700 mb-[40px]">
          frequently asked questions
        </p>
        <div className="flex flex-col justify-between w-full mb-5">
          <CustomizedAccordions
            data={list}
            expanded={expanded}
            handleChange={handleChangeAct}
          />
        </div>
        <div className="flex justify-center w-full md:px-10">
          <PaginationBox
            page={page}
            count={totalPage}
            onChange={handleChangePage}
          />
        </div>
      </div>
    </div>
  );
}

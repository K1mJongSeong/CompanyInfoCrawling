import client from "./api/client";

export interface InFaqProps {
  answer: string;
  create_at: string;
  exposure: string;
  modified_at: string;
  page_num: string;
  qna_id: number;
  question: string;
  question_content: string;
  total_page_num: string;
  writer: string;
}

export const getQnaList = async ({ page }: { page?: string }) => {
  const res = await client.get(`/QnaListAPI/${page ? page : "1"}`);
  const data = await res.data;
  return data;
};

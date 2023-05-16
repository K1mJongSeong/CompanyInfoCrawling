import client from "./api/client";

export const getQnaList = async ({ page }: { page?: string }) => {
  const res = await client.get(`/QnaListAPI/${page ? page : "1"}`);
  const data = await res.data;
  return data;
};

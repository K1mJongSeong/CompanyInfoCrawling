import ServiceContainer from "@/containers/service/ServiceContainer";
import { getQnaList } from "@/service/service_service";

export const revalidate = 3;

export default async function ServicePage() {
  const qnaList = await getQnaList({ page: "1" });

  return <ServiceContainer qnaList={qnaList} />;
}

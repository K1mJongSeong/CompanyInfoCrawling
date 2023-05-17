import FaqsContainer from "@/containers/service/FaqsContainer";

export const revalidate = 3;

export default async function FaqsPage() {
  return <FaqsContainer />;
}

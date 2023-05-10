import SearchContainer from "@/containers/search/SearchContainer";

interface Props {
  params: {
    slug: Array<string>;
  };
}
export default function SearchPage({ params: { slug } }: Props) {
  return <SearchContainer slug={slug} />;
}

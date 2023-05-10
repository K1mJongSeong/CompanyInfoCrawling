"use client";

import PaginationBox from "@/components/common/Pagination";
import NoSearch from "@/components/search/NoSearch";
import SearchList, { SearchItem } from "@/components/search/SearchList";
import SearchTop from "@/components/search/SearchTop";
import { SearchCard, SearchLayoutContainer } from "@/components/search/styles";
import { Stack, Typography } from "@mui/material";
import { useEffect, useState } from "react";
interface Props {
  slug: Array<string>;
}
export default function SearchContainer({ slug }: Props) {
  const [searchValue, setSearchValue] = useState<string>("");
  useEffect(() => {
    if (slug) {
      setSearchValue(decodeURI(decodeURIComponent(slug[0])));
    } else {
      setSearchValue("");
    }
  }, [slug]);
  const [result, setResult] = useState(false);
  return (
    <SearchLayoutContainer>
      <SearchTop searchValue={searchValue} />
      <SearchCard>
        <Stack direction={"row"} mb={3} gap={1} alignItems={"flex-end"}>
          <Typography variant="h2" fontSize={"large"} fontWeight={"bold"}>
            {searchValue}
          </Typography>
          <Typography variant="body1" fontSize={"small"}>
            Search Reasult 0000
          </Typography>
        </Stack>
        {result ? (
          <>
            <SearchList>
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
              <SearchItem />
            </SearchList>
            <PaginationBox />
          </>
        ) : (
          <NoSearch />
        )}
      </SearchCard>
    </SearchLayoutContainer>
  );
}

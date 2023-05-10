import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { Pagination } from "@mui/material";

export const StyledPagination = styled(Pagination)`
  .MuiPagination-ul {
    flex-wrap: nowrap !important;
  }
  ${media.tablet} {
    .MuiButtonBase-root {
      min-width: 24px;
      height: 24px;
    }
  }
`;

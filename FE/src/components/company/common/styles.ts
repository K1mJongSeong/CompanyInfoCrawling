import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { Box, Button } from "@mui/material";
import { grey } from "@mui/material/colors";

export const CompanyLayoutContainer = styled(Box)`
  max-width: 1586px;
  display: flex;
  flex-direction: column;
  height: max-content;
  margin: 0 auto;
  padding-bottom: 100px;
  position: relative;
  padding-top: 50px;

  ${media.tablet} {
    padding-top: 35px;
  }
`;

export const CompanyTopBgBox = styled(Box)`
  width: 100%;
  height: 80px;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 6;
  border-radius: 0 0 80px 80px;
  /* Permalink - use to edit and share this gradient: https://colorzilla.com/gradient-editor/#5b7fff+0,7654ff+100 */
  background: #5b7fff; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* FF3.6-15 */
  background: -webkit-linear-gradient(
    -45deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    135deg,
    #5b7fff 0%,
    #7654ff 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#5b7fff', endColorstr='#7654ff',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
`;

export const CompanyCard = styled(Box)`
  width: calc(100% - 32px);
  max-width: 1388px;
  background-color: white;
  border-radius: 8px;
  margin: 0 auto;
  box-shadow: 4px 4px 20px rgba(23, 33, 122, 0.3);
  padding: 25px 1rem 56px;
  position: relative;
  z-index: 7;
`;
export const BorderCompanyCard = styled(Box)`
  width: 100%;
  min-height: 347px;
  border-radius: 5px;
  padding: 36px 50px;
  border: 1px solid #a7a7ce;
  background: #f1f4ff; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* FF3.6-15 */
  background: -webkit-linear-gradient(
    -45deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    135deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f1f4ff', endColorstr='#7db9e8',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */

  ol,
  ul,
  li {
    list-style: initial;
    color: ${grey[400]};
  }
  ${media.tablet} {
    padding: 28px 20px;
    min-height: auto;
  }
`;

export const StyledBtn = styled(Button)`
  min-width: auto;
  width: 40px;
  height: 40px;
  padding: 0;
`;

import { useState } from "react";
import type { ImageProps } from "next/image";
import Image from "next/image";
import styled from "@emotion/styled";

const ImageLoader = ({ src }: { src: string }) => {
  const imageSrc = `${src}`;
  return imageSrc;
};

const Img = (props: ImageProps) => {
  const [loading, setLoading] = useState<boolean>(true);

  return (
    <ImgBlock
      {...props}
      loader={ImageLoader}
      layout="fill"
      onLoadingComplete={() => setLoading(false)}
    />
  );
};

const ImgBlock = styled(Image)`
  height: auto !important;
  position: relative !important;
`;

export default Img;

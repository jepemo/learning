repList :: Int -> Int -> [Int]
repList n e
    | n == 0 = return []
    | otherwise = return ([e] ++ (repList n-1 e))

f :: Int -> [Int] -> [Int]
f n arr =
    map (repList n) arr

-- This part handles the Input and Output and can be used as it is. Do not modify this part.
main :: IO ()
main = getContents >>=
       mapM_ print. (\(n:arr) -> f n arr). map read. words

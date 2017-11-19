import Control.Applicative
import Control.Monad
import System.IO

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    --  Print "Hello World" on a new line 'n' times.
    hello_worlds n

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret   
        
hello_worlds n
    | n == 1 = do
        putStrLn "Hello World"
    | otherwise = do
        putStrLn "Hello World"
        hello_worlds (n-1)

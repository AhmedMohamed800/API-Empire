const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');

module.exports = {
    mode: "development",
    entry: {
        bundle: path.resolve(__dirname, "src/main.tsx"),
    },
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "[name][contenthash].js",
        clean: true,
        assetModuleFilename: '[name][ext]'
    },
    module:{
        rules: [
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader']
            },
            {
                test: /\.(js|jsx|tsx|ts)$/i,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', "@babel/preset-react", '@babel/preset-typescript']
                    }
                }
            },
            {
                test: /\.(png|jpg|gif|jpeg|svg)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'assets/[hash][ext][query]'
                  }
            }
        ]
    },
    devServer:{
        static: {
            directory: path.resolve(__dirname, 'dist')
        },
        port: 3333,
        open: true,
        hot: true,
        compress: true,
        historyApiFallback: true,
    },
    // devtool: "source-map",
    plugins:[
        new MiniCssExtractPlugin({
            filename: "style.css",
            chunkFilename: "index.css"
          }),
        new HtmlWebpackPlugin({
            title: "React App",
            filename: "index.html",
            template: "public/index.html"
        }),
        new Dotenv({
            path: './src/.env'
        })
    ]
}
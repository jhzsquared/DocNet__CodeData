
import pandas as pd
from newsnet_utils import NewsCorpus, AugmentedTextGraph, process_text, AugmentedTextGraphSentiment
import sys
from concurrent.futures import ThreadPoolExecutor

def process_text_errors(id_text):
        #process text wrapped to handle errors and use in threadpool
        #input as tuple
        id = id_text[0]
        text = id_text[1]
        try:
            sentences = process_text(text)
        except IndexError:
            print("weird contraction error, skipping document")
            sentences = None
        return id, sentences

def process_full_data(data_path):
    if data_path[-3:]=="pkl":
        text_df = pd.read_pickle(data_path)
    elif data_path[-3:] == "csv":
        text_df = pd.read_csv(data_path)
    print(text_df.shape)
    print(text_df.shape)

    #build various datasets 
    process_data_path = data_path.replace('/raw/', '/processed/')
    process_data_path = process_data_path.replace('.csv', '.pkl')
    copy_text_df = text_df.copy()

    #break data into sentences first since all model datasets use that as base block to create graph etc.
    sentences_list = []
    skip_index = []

    with ThreadPoolExecutor() as executor:
        for id, sentences in executor.map(process_text_errors, zip(text_df.index,text_df["text"])):
            sentences_list.append(sentences)
            if sentences is None:
                skip_index.append(id)

    #remove skipped documents
    copy_text_df = text_df[~text_df.index.isin(skip_index)]
    sentences_list = [sentences for sentences in sentences_list if sentences is not None]

    #Doc2vec
    doc2vec_data = [doc for doc in NewsCorpus(sentences_list)]#use full data to establish vocab
    copy_text_df["doc2vec_data"] = doc2vec_data 
    print(len(doc2vec_data))

    #graph2vec networkx graphs (regular and sentiment)
    g2v_graphs = []
    g2v_graphs_sent = []
    skip_index = []
    i=0
    for sentences in sentences_list:
        try: 
            G = AugmentedTextGraph().makenx_graph(sentences)
            G2 = AugmentedTextGraphSentiment().makenx_graph(sentences)
            g2v_graphs.append(G)
            g2v_graphs_sent.append(G2)
        except ValueError as e:
            if str(e) == "There are no co-occurring words in this document":
                print("skipping text: {}".format(str(e)))
                skip_index.append(text_df.index[i])
                g2v_graphs.append(None) #make it blank
                g2v_graphs_sent.append(None)
            else: #new unexpected error (maybe deal with)
                print(e)
                skip_index.append(text_df.index[i])
                g2v_graphs.append(None) #make it blank
                g2v_graphs_sent.append(None)
        i+=1
        
    print(len(g2v_graphs))
    print("skipped {} documents".format(len(skip_index)))
    print(skip_index)
    copy_text_df["graph2vec_data"] = g2v_graphs
    copy_text_df["graph2vec_data_sent"] = g2v_graphs_sent

    #AE graphs

    #Make data into graph
    ae_dataset = []
    ae_sent_dataset = []
    skip_index = []
    i=0
    for sentences in sentences_list:
        try: 
            G = AugmentedTextGraph().create_augmented_text_graph(sentences)
            G2 = AugmentedTextGraphSentiment().create_augmented_text_graph(sentences)
            ae_dataset.append(G)
            ae_sent_dataset.append(G2)
        except ValueError as e:
            if str(e) == "There are no co-occurring words in this document":
                print("skipping text: {}".format(str(e)))
                skip_index.append(text_df.index[i])
                ae_dataset.append(None) #make it blank
                ae_sent_dataset.append(None)
            else: #new unexpected error
                print(e)
                skip_index.append(text_df.index[i])
                ae_dataset.append(None) #make it blank
                ae_sent_dataset.append(None)
        i+=1
        
    print(len(ae_dataset))
    copy_text_df["autoencode_data"] = ae_dataset
    copy_text_df["autoencode_data_sent"] = ae_sent_dataset

    #transformer sentences
    sbert_sentences = []
    for sentences in sentences_list:
        sentences = [str(sent) for sent in sentences]
        sbert_sentences.append(sentences)

    print(len(sbert_sentences))
    copy_text_df["transformer_data"] = sbert_sentences

    #save it out to pickle
    copy_text_df.to_pickle(process_data_path)

if __name__ == "__main__":
    data_path = sys.argv[1] 
    process_full_data(data_path)
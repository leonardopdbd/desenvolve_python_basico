import emoji

def main():
    # Exibe os emojis disponíveis com seus códigos correspondentes
    print("Emojis disponíveis:")
    print("❤️ - :red_heart:")
    print("👍 - :thumbs_up:")
    print("🤔 - :thinking_face:")
    print("🥳 - :partying_face:")
    
    # Solicita uma frase com emojis codificados ao usuário
    frase_codificada = input("\nDigite uma frase e ela será emojizada: ")
    
    # Emojiza a frase usando emoji.emojize()
    frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
    
    # Exibe a frase emojizada
    print("Frase emojizada:")
    print(frase_emojizada)

if __name__ == "__main__":
    main()
